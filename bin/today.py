#!/usr/bin/env python3
"""今天该联系谁。

读取人物档案 CSV，按"距上次联系天数 / 目标频率"排序，打出今天最该联系的人
和联系时用得上的上下文。

  python3 bin/today.py                 # 默认读 roster.csv
  python3 bin/today.py 路径.csv -n 5   # 指定文件，列出 5 个
  python3 bin/today.py --done 王某某   # 把某人的"上次联系"改成今天

档案字段见 templates/roster.template.csv。真实档案不要提交到公开仓库。
"""
import argparse
import csv
import datetime as dt
import sys

FIELDS = ["姓名", "圈层", "关系", "现在做什么", "所在地", "配偶", "子女",
          "他关心什么", "我能给什么", "目标频率天", "上次联系", "最近聊了什么", "备注"]


def parse_date(s):
    s = (s or "").strip()
    if not s:
        return None
    for fmt in ("%Y-%m-%d", "%Y/%m/%d", "%Y.%m.%d"):
        try:
            return dt.datetime.strptime(s, fmt).date()
        except ValueError:
            continue
    return None


def load(path):
    try:
        with open(path, newline="", encoding="utf-8-sig") as f:
            return list(csv.DictReader(f))
    except FileNotFoundError:
        sys.exit(f"找不到 {path}。先从 templates/roster.template.csv 复制一份，"
                 f"填上真实的人，存成 roster.csv（已在 .gitignore 里）。")


def overdue_ratio(row, today):
    """>1 表示已经超过目标频率。从未联系过的排最前。"""
    try:
        cadence = float(row.get("目标频率天") or 60)
    except ValueError:
        cadence = 60.0
    cadence = max(cadence, 1.0)
    last = parse_date(row.get("上次联系"))
    if last is None:
        return float("inf")
    return (today - last).days / cadence


def show(row, today):
    last = parse_date(row.get("上次联系"))
    gap = "从未联系" if last is None else f"{(today - last).days} 天前"
    print(f"\n  {row.get('姓名','?')}  [{row.get('圈层','')}/{row.get('关系','')}]  上次：{gap}")
    for label, key in (("在做", "现在做什么"), ("在", "所在地"), ("子女", "子女"),
                       ("他关心", "他关心什么"), ("我能给", "我能给什么"),
                       ("上次聊", "最近聊了什么"), ("备注", "备注")):
        v = (row.get(key) or "").strip()
        if v:
            print(f"    {label}：{v}")


def main():
    ap = argparse.ArgumentParser(description="今天该联系谁")
    ap.add_argument("path", nargs="?", default="roster.csv", help="档案 CSV（默认 roster.csv）")
    ap.add_argument("-n", type=int, default=3, help="列出几个（默认 3）")
    ap.add_argument("--done", metavar="姓名", help="把此人的『上次联系』标为今天")
    args = ap.parse_args()

    today = dt.date.today()
    rows = load(args.path)
    if not rows:
        sys.exit("档案是空的。")

    if args.done:
        hit = [r for r in rows if (r.get("姓名") or "").strip() == args.done.strip()]
        if not hit:
            sys.exit(f"档案里没有『{args.done}』。")
        for r in hit:
            r["上次联系"] = today.isoformat()
        with open(args.path, "w", newline="", encoding="utf-8") as f:
            w = csv.DictWriter(f, fieldnames=rows[0].keys())
            w.writeheader()
            w.writerows(rows)
        print(f"已记录：{args.done} 于 {today} 联系过。别忘了把聊了什么补进『最近聊了什么』。")
        return

    ranked = sorted(rows, key=lambda r: -overdue_ratio(r, today))
    due = sum(1 for r in rows if overdue_ratio(r, today) >= 1)
    print(f"{today}　档案 {len(rows)} 人，其中 {due} 人已到该联系的时候。")
    print("带一样东西去，不要空手问『在吗』。")
    for row in ranked[: max(args.n, 1)]:
        show(row, today)
    print(f"\n联系完了记一笔：python3 {sys.argv[0]} --done 姓名\n")


if __name__ == "__main__":
    main()
