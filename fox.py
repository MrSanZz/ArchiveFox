import requests, sys, os, ijson

url = 'https://web.archive.org/web/timemap/json?url={}&matchType=prefix&collapse=urlkey&output=json&fl=original%2Cmimetype%2Ctimestamp%2Cendtimestamp%2Cgroupcount%2Cuniqcount&filter=!statuscode%3A%5B45%5D..&limit={}&_=1772121893078'

def filtering(dom: str, limit: str):
    global url
    total = int(limit)
    count = 0

    try:
        with requests.get(
            url.format(dom, limit),
            headers={"Accept": "application/json"},
            stream=True
        ) as resp:

            resp.raw.decode_content = True
            items = ijson.items(resp.raw, 'item')

            for item in items:
                print(item[0])
                count += 1

                last_progress = -1

                progress = int((count / total) * 100)
                if progress != last_progress:
                    sys.stderr.write(f"\r[+] Progress: {progress}%")
                    sys.stderr.flush()
                    last_progress = progress

    except KeyboardInterrupt:
        sys.exit(0)

def return_true():
    return True

def main():
    try:
        url = sys.argv[1];limit = sys.argv[2]

        if int(limit) >= 1000000:
            print("WARNING: The amount of limit you input is exceeding the capacity limit")
            y=input("Continue action? Y/N: ") or 'n'
            return_true() if y.lower() =='y' else os._exit(9)
        outp = filtering(url, limit)
        print(outp)
    except IndexError:
        f=''.join(__file__.split('\\')[-1]) if os.name == 'NT' else ''.join(__file__.split('/')[-1])
        print(f"Usage: python3 {f} <domain> <limit>")

if __name__ == '__main__':
    main()
