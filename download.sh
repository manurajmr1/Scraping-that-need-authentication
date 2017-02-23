filename='videos.txt'
i=0
while read p; do 
    i=$((i+1)) 
    wget -O $i.mp4 $p --user-agent="Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.6) Gecko/20070725 Firefox"
done < $filename
