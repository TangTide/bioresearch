from Bio import Entrez

Entrez.email = ""
Entrez.api_key = ""
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
