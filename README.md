## housing_price_predictor
This is a machine Learning project for housing price prediction
### Software and account Requirement.

1. [Github Account](https://github.com)
2. [Heroku Account](https://dashboard.heroku.com/login)
3. [VS Code IDE](https://code.visualstudio.com/download)
4. [GIT cli](https://git-scm.com/downloads)
5. [GIT Documentation](https://git-scm.com/docs/gittutorial)


Creating conda environment
```
conda create -p venv python==3.7 -y
```
```
conda activate venv/
```
OR 
```
conda activate venv
```

```
pip install -r requirements.txt
```
add files to git repo
```
git add .
```
git commit -m "your message"
```
git push origin main
```

To setup CI/CD(Continuous integration/deployment) pipeline in heroku , we need 3 informations
1. HEROKU_EMAIL = technidata225@gmail.com
2. HEROKU_API_KEY = f43db5dd-d91a-4f6f-9110-b1f7fed29f6e
3. HEROKU_APP_NAME = innovia-housing-price

Building Docker image
```
docker build -t <image_name>:<tag_name> .
```

List docker image
```
docker images
```
Run docker image
```
docker run -p 5000:5000 -e PORT=5000 <image_id>
```
To check running container
```
docker ps
```
to stop docker 
```
docker stop <container_id>
```

