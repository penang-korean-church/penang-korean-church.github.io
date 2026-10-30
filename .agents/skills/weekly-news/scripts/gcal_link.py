#!/usr/bin/env python3
"""Google Calendar '캘린더에 추가' 링크 생성기.

사용 예:
  python3 gcal_link.py "10월 온가족 기도회" 2026-10-30 20:00 --minutes 90
  python3 gcal_link.py "11월 성찬예배" 2026-11-01 11:00 --end 12:30 --details "페낭한인교회 11월 성찬예배"
  python3 gcal_link.py "세례 교육 (1회)" 2026-10-25 10:00 --markdown   # 마크다운 링크 형태로 출력

details를 생략하면 "페낭한인교회 <제목>"이 들어갑니다. 장소는 항상 교회 주소, 시간대는 Asia/Kuala_Lumpur.
"""
import argparse
from datetime import datetime, timedelta
from urllib.parse import quote

LOCATION = "598-01-02, Menara Asas, Tanjung Bungah, 11200, Penang, Malaysia"
TZ = "Asia/Kuala_Lumpur"


def build(title, date, start, end=None, minutes=90, details=None):
    s = datetime.strptime(f"{date} {start}", "%Y-%m-%d %H:%M")
    e = datetime.strptime(f"{date} {end}", "%Y-%m-%d %H:%M") if end else s + timedelta(minutes=minutes)
    details = details or f"페낭한인교회 {title}"
    q = lambda v: quote(v, safe="")
    return (
        "https://calendar.google.com/calendar/render?action=TEMPLATE"
        f"&text={q(title)}"
        f"&dates={s:%Y%m%dT%H%M%S}/{e:%Y%m%dT%H%M%S}"
        f"&details={q(details)}"
        f"&location={q(LOCATION)}"
        f"&ctz={TZ}"
    )


if __name__ == "__main__":
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("title")
    ap.add_argument("date", help="YYYY-MM-DD")
    ap.add_argument("start", help="HH:MM (24시간)")
    ap.add_argument("--end", help="HH:MM. 없으면 --minutes 사용")
    ap.add_argument("--minutes", type=int, default=90, help="기본 90분")
    ap.add_argument("--details", help="기본: '페낭한인교회 <제목>'")
    ap.add_argument("--markdown", action="store_true", help="'📅 [캘린더에 추가](URL)' 형태로 출력")
    a = ap.parse_args()
    url = build(a.title, a.date, a.start, a.end, a.minutes, a.details)
    print(f"📅 [캘린더에 추가]({url})" if a.markdown else url)
