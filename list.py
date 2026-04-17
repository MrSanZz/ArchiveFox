import requests, sys

def check(filename):
    total=0;count=0;valid=0;list_valid=[];decount=0
    content=open(filename, 'r').read().split()
    for _ in range(len(open(filename, 'r').read().split())):
        total+=1
    print(f"[+] Total URL: {total}")
    while True:
        try:
         ongoing=content[count]
        except:
         print("[!] Done")
         return list_valid
        if "http" in ongoing:
            print(f"[?] Checking: {ongoing}...")
            try:
             response=requests.get(ongoing, timeout=20).status_code
            except:
             response=0
            if response == 200:
                valid+=1
                list_valid.append(ongoing)
                print(f"[!] {ongoing} - 200")
                count+=1
            else:
                count+=1
                continue
        else:
            decount+=1;count+=1
            continue
        total_value = total-decount
        if count == total_value:
            print("[!] Done")
            return list_valid

if __name__ == '__main__':
    file=sys.argv[1];save_as=sys.argv[2]
    results=check(file)
    for i in results:
        print(i)
        open(save_as, 'a').write(str(i)+"\n")
