from Bio import Entrez

Entrez.email = "tangtide1@tangtide.com"
Entrez.api_key = "6710abb71acd59b3d7a7fa0e15b39cd02b09"
ids = [29845521]
ida = []
for id1 in ids:
    try:
        results = Entrez.read(Entrez.elink(dbfrom="pubmed", db="pmc", LinkName="pubmed_pmc_refs", id=id1))
        pmc_ids = [link["Id"] for link in results[0]["LinkSetDb"][0]["Link"]]
        print(len(pmc_ids))
        print(pmc_ids)
        ida = ida + pmc_ids
    except:
        print("NONE")
