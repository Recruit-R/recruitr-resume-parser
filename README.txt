resume parser for senior project

Mkae sure this version of spacey is installed

1. python -m pip install https://github.com/explosion/spacy-models/releases/download/en_core_web_sm-2.3.1/en_core_web_sm-2.3.1.tar.gz


run these commands in order in the cloud shell

1.  docker build -t gcr.io/certain-tendril-419122/resume-parser:v2 .

2.  gcloud auth configure-docker

3.  docker tag gcr.io/certain-tendril-419122/resume-parser:v2 gcr.io/certain-tendril-419122/resume-parser:v2

4.  docker push gcr.io/certain-tendril-419122/resume-parser:v2

5.  gcloud config set run/region us-east5

6.  gcloud run deploy --image=gcr.io/certain-tendril-419122/resume-parser:v2 --platform=managed

you can test the deploy with this command
curl command
curl -X POST https://resume-parser-upglu46dla-ul.a.run.app -H "Content-Type: application/json" -d '{"data": "'$(base64 -w 0 ../OmkarResume.pdf)'" }'
