# Eventex
Sistema de eventos organizado pelo WTTD

## Como desenvolver?

1. Clone repositório.
2. Crie um virtualenv com python 3.6
3. Ative seu virtualenv.
4. Instale as dependências.
5. Execute os testes.

```console
git clone git@github.com:zeny-brus/wttd-eventex.git wttd
cd wttd
python -m venv .wttd
source .wttd/bin/activate
pip install -r requirements-dev.txt
cp contrib/env-sample .env
python manage.py test 
```
## Como fazer o deploy?

1. Crie uma instância no Heroku
2. Envie as configurações para o Heroku
3. Define uma SECRET_KEY segura para a instância
4. Defina DEBUG=False
5. Configure o serviço de e-mail
6. Envie o código para o Heroku

```console
heroku create minhainstancia
heroku config:push
heroku config:set SECRET_KEY=`python contrib/secret_gen.py`
heroku config:set DEBUG=False
#configuro o e-mail
git push heroku master --force
```
