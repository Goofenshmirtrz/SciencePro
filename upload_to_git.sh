while [ 0 -ge 0 ]
do
    sleep 3600
    git add *.txt
    git commit -m "Upload sensor data "
    git push origin HEAD
done