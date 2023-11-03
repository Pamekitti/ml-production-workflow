# ML Deployment with BentoML

## Steps
- download and register model to bentoml local storage: `python3 prepare_model.py`
- check model list: `bentoml models list`
- ml serving from service script: `bentoml serve service.py`
- update `bentofile.yaml`
- build a bento: `bentoml build`
- check available bento: `bentoml list`
- ml serving from available bento: `bentoml serve summarization:latest --production`
- dockerize the target bento: `bentoml containerize --opt platform=linux/arm64/v8 summarization:latest`
- check all docker images: `docker images`
- run and deploy docker container: `docker run -itd --name bentoml-local -p 3000:3000 summarization:ikzrpyd2tcmftmur`

Bugs on running transformers models
- https://github.com/bentoml/BentoML/issues/4238
