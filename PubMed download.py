from Bio import Entrez
import http.client

http.client.HTTPConnection._http_vsn = 10
http.client.HTTPConnection._http_vsn_str = 'HTTP/1.0'
Entrez.email="tangtide1@tangtide.com"
Entrez.api_key="6710abb71acd59b3d7a7fa0e15b39cd02b09"
# Entrez.email = "abc@exampl.com"  # 你的邮箱
# Entrez.api_key = "6710abb71acd59a5d7a7fh6f15b39cd02b09"  # 你的API
mindate_ = "2013/1/1"  # 论文的时间跨度
maxdate_ = "2016/12/31"
filename = "pubmed2013-2016.txt"#保存的文件名
keyword = "(arthropod borne virus) OR (arboviral disease)"  # 搜索关键词
search_results = Entrez.read(
    Entrez.esearch(
        db="pubmed",
        term=keyword,  # 关键词
        datetype="pdat",
        usehistory="y",  # 是否使用历史记录，y可优化搜索
        mindate=mindate_, maxdate=maxdate_  # 论文的时间跨度
    )
)
count = int(search_results["Count"])
print("Found %i results" % count)
batch_size = 2000  # 单次下载的文章数，可依据自身网速调整
out_handle = open("filename", 'w', encoding='utf-8')
for start in range(0, count, batch_size):
    end = min(count, start + batch_size)
    print("Going to download record %i to %i" % (start + 1, end))
    fetch_handle = Entrez.efetch(
        db="pubmed",
        rettype="medline",
        retmode="text",
        retstart=start,
        retmax=batch_size,
        webenv=search_results["WebEnv"],
        query_key=search_results["QueryKey"],
    )
    data = fetch_handle.read()
    fetch_handle.close()
    out_handle.write(data)
out_handle.close()