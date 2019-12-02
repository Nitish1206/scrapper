import wget
import csv
output_path = '/media/nitish/Work/Work/scrapping/output_images'
with open('/media/nitish/Work/Work/scrapping/image_link.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if not row:
            continue
        print(row[1])
        try:
            wget.download(url=row[1], out='/media/nitish/Work/Work/scrapping/output_images')
        except Exception as e:
            print(e)
            pass