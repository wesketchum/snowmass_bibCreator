import sys,os

hyperlink_pretext = "https://www.snowmass21.org/docs/files/summaries/"
file_name_starter="SNOWMASS21-"

with open("IF4.csv") as f_in:
    lines = f_in.readlines()
    for line in lines[1:]:
        split_lines = line.split(";")
        title = split_lines[1]
        file_name = split_lines[0]
        frontier = file_name[len(file_name_starter):len(file_name_starter)+2]
        if(frontier=='Co'):
            frontier="CompF"
        loi_id = "LOI_"+frontier+file_name[-7:-4]
        hyperlink = hyperlink_pretext+frontier+"/"+file_name
        lead_author = split_lines[3]
        
        print("@misc{%s,"%loi_id)
        print("  title = {%s},"%title)
        print("  author = {%s and others},"%lead_author)
        print("  year = {2020},")
        print("  howpublished = {Snowmass2021 LOI},")
        print("  note = \url{%s},"%hyperlink)
        print("}")

        #print(title,hyperlink,loi_id)

sys.exit()
