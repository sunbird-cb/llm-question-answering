Here is the example we discussed during the meeting

 

 

{

    "docID": "",

    "docPath": https://path to a pdf (or "docPath": "/home/divyansh/mydata/doc1.pdf")

 

}

 

    DocExtractor (Subscriber 1)

 

{

    "docID": "",

    "docPath": https://path to a pdf,  (or "docPath": "/home/divyansh/mydata/doc1.pdf")

    "docContents": "Text extracted from the pdf"

}   

 

    DocEnrich (Subscriber 2)

 

{

    "docID": "",

    "docPath": https://path to a pdf,  (or "docPath": "/home/divyansh/mydata/doc1.pdf")

    "docContents": "Text extracted from the pdf",

    "docSnippets": [

        "para 1",

        "para 2"

    ]  

}

 

    DocStore (Subscriber 3)

 

Each Snippet ingest to the selected vector store  