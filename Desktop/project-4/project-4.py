import datetime, time
import urllib.request

url = "https//americanhumanist.org/what-is-humanism/definition-of-humanism/"


f= urllib.request.urlopen(url)
#data = f.read().decode('euc-kr')
data = f.read().decode('utf-8')

begin = data.find("Humanism is a progressive lifestance")
end = data.find("Joseph C. Sommer")

end += len("Joseph C. Sommer")

print("total=",len(data))
print("begin=",begin)
print(data[begin:beginbegin+100])
print(data[end-100:end])
print("length=", end-begin)

speech = data[begin:end]
speech = speech.split()
#print(speech[:100])

analyze = {}

for word in speech:
    analyze[word] = analyze.get(word, 0) + 1

flist = sorted(analyze.items(), key=lambda kv: kv[1], reverse=True)
print("number of words id ", len(flist))

cnt = 0
for k, v in flist
print(k, v)
if cnt > 100:break
cnt += 1












    
