#!/usr/bin/env python3
"""성서유니온 〈매일성경 오디오 해설〉 재생목록에서 해당 주 본문 영상을 찾습니다.

사용 예:
  python3 find_daily_bible_video.py                 # 최근 영상 전체 목록 (videoId, 제목)
  python3 find_daily_bible_video.py 야고보서 5      # 제목에 '야고보서'와 '5'가 모두 들어간 영상만
  python3 find_daily_bible_video.py --date 2026-10-25   # 해당 날짜 본문 영상 (제목이 「2026년 10월 25일 | 매일성경」 으로 시작)
  python3 find_daily_bible_video.py --limit 40

출력: videoId <TAB> watch URL <TAB> 제목. 나눔지 본문 날짜(주일)에 해당하는 영상을 쓰면 됩니다.

YouTube 재생목록 RSS는 404를 내므로 재생목록 HTML의 ytInitialData를 직접 긁습니다.
영상은 보통 해당 본문 날짜 당일에 올라오므로, 아직 없으면 그 사실을 보고하고 임베드는 비워두지 말고
재생목록 전체 링크만 남깁니다.
"""
import json
import re
import sys
import urllib.request

PLAYLIST = "PLXD3svvkQBPHews8RDWcGqCDag563R2lr"
URL = f"https://www.youtube.com/playlist?list={PLAYLIST}"
UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36"


def fetch_videos():
    req = urllib.request.Request(URL, headers={"User-Agent": UA, "Accept-Language": "ko,en;q=0.8"})
    html = urllib.request.urlopen(req, timeout=20).read().decode("utf-8", "replace")
    m = re.search(r"ytInitialData\s*=\s*(\{.*?\});\s*</script>", html, re.S)
    if not m:
        sys.exit("ytInitialData를 찾지 못했습니다. YouTube 페이지 구조가 바뀌었을 수 있습니다.")
    data = json.loads(m.group(1))
    out = []

    def walk(node):
        # 2026년 현재 YouTube 재생목록은 lockupViewModel 안에 contentId + metadata.title.content 로 영상을 담습니다.
        if isinstance(node, dict):
            r = node.get("lockupViewModel")
            if r and r.get("contentId"):
                title = (r.get("metadata", {}).get("lockupMetadataViewModel", {})
                          .get("title", {}).get("content", ""))
                out.append((r["contentId"], title))
            for v in node.values():
                walk(v)
        elif isinstance(node, list):
            for v in node:
                walk(v)

    walk(data)
    return out


if __name__ == "__main__":
    argv = sys.argv[1:]
    limit = 100
    args = []
    i = 0
    while i < len(argv):
        if argv[i] == "--limit":
            limit = int(argv[i + 1]); i += 2
        elif argv[i] == "--date":
            y, m, d = argv[i + 1].split("-")
            args.append(f"{int(y)}년 {int(m)}월 {int(d)}일"); i += 2
        else:
            args.append(argv[i]); i += 1
    videos = fetch_videos()
    hits = [(vid, t) for vid, t in videos if all(k in t for k in args)]
    if not hits:
        print(f"'{' '.join(args)}' 에 해당하는 영상이 없습니다. (총 {len(videos)}개 확인)")
        sys.exit(1)
    for vid, t in hits[:limit]:
        print(f"{vid}\thttps://www.youtube.com/watch?v={vid}&list={PLAYLIST}\t{t}")
