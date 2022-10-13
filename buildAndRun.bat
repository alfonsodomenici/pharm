docker build -t pharm .
docker rm -f   pharm
docker run -d --name pharm -p80:5000 pharm