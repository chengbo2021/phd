#!/usr/bin/env python3
"""博士圈缺口图：产品缺的每一块，名单里谁能补，哪块还没人。

读取博士圈档案 CSV 的"能补的缺口"列（分号分隔的标签），按
phd-network.zh-CN.md 第 2 节的缺口清单和位置清单逐项列出谁能补，
并单独列出独立评审候选。

  python3 bin/phd_gaps.py                    # 默认读 roster-phd.csv
  python3 bin/phd_gaps.py 路径.csv
  python3 bin/phd_gaps.py templates/roster-phd.template.csv   # 用示例数据试跑

档案字段见 templates/roster-phd.template.csv。真实档案不要提交到公开仓库。
联系节奏仍用 bin/today.py，它能直接读同一份档案。
"""
import argparse
import csv
import re
import sys

# 与 phd-network.zh-CN.md 第 2 节一一对应，改一边要改另一边。
GAPS = ["微生物", "不确定度", "通量数据", "遥感", "机器学习", "水文", "农学",
        "土壤生物炭", "农经", "碳市场法规", "软件工程", "融资"]
DOORS = ["越南", "印度", "菲律宾", "孟加拉", "印尼", "泰国", "巴西", "加州",
         "IRRI", "CGIAR", "世界银行", "FAO", "碳公司", "核证机构", "大厂", "咨询"]


def load(path):
    try:
        with open(path, newline="", encoding="utf-8-sig") as f:
            return list(csv.DictReader(f))
    except FileNotFoundError:
        sys.exit(f"找不到 {path}。先从 templates/roster-phd.template.csv 复制一份，"
                 f"填上真实的人，存成 roster-phd.csv（已在 .gitignore 里）。")


def tags(row):
    raw = row.get("能补的缺口") or ""
    return {t.strip() for t in re.split(r"[;；,，、]", raw) if t.strip()}


def is_reviewer(row):
    return (row.get("独立评审候选") or "").strip() in ("是", "y", "yes", "Y", "Yes")


def label(row):
    name = (row.get("姓名") or "?").strip()
    where = "/".join(v for v in ((row.get("机构") or "").strip(),
                                 (row.get("国家") or "").strip()) if v)
    return f"{name}（{where}）" if where else name


def section(title, keys, rows):
    print(f"\n{title}")
    empty = []
    for k in keys:
        who = [label(r) for r in rows if k in tags(r)]
        if who:
            print(f"  {k:<6}  " + "、".join(who))
        else:
            empty.append(k)
    return empty


def main():
    ap = argparse.ArgumentParser(description="博士圈缺口图")
    ap.add_argument("path", nargs="?", default="roster-phd.csv",
                    help="博士圈档案 CSV（默认 roster-phd.csv）")
    args = ap.parse_args()

    rows = load(args.path)
    if not rows:
        sys.exit("档案是空的。")

    reviewers = [r for r in rows if is_reviewer(r)]
    # 评审候选不算进合作覆盖：他们要留在合作圈外。
    pool = [r for r in rows if not is_reviewer(r)]

    print(f"博士圈 {len(rows)} 人，其中可合作 {len(pool)} 人，独立评审候选 {len(reviewers)} 人。")
    gap_empty = section("产品缺口：谁能补", GAPS, pool)
    door_empty = section("客户的门：谁在那", DOORS, pool)

    known = set(GAPS) | set(DOORS)
    untagged = [label(r) for r in pool if not tags(r)]
    unknown = sorted({t for r in pool for t in tags(r)} - known)

    print("\n还没人的缺口：" + ("、".join(gap_empty) if gap_empty else "无"))
    print("还没门的地方：" + ("、".join(door_empty) if door_empty else "无"))
    if gap_empty:
        print("  下一步：问名单上已有的人『你认识做这个的人吗』。")

    print("\n独立评审候选（只请教，不合著、不当顾问、不给期权）：")
    if reviewers:
        for r in reviewers:
            print(f"  {label(r)}  学科：{(r.get('学科') or '').strip() or '?'}")
    else:
        print("  还没有。从最懂生物地球化学模型的人里留一到两个。")
    if any((r.get("合作形式") or "").strip()[:1] in list("34567") for r in reviewers):
        print("  注意：有评审候选的『合作形式』在第 3 级以上，会过不了利益冲突审查。")

    if untagged:
        print("\n没填缺口的人：" + "、".join(untagged))
    if unknown:
        print("不在清单里的标签（检查拼写，或补进 GAPS/DOORS）：" + "、".join(unknown))
    print()


if __name__ == "__main__":
    main()
