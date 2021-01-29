import os


# create new directory for each crawl proj
def create_project_directory(directory):
    if not os.path.exists(directory):
        print('Creating the directory')
        os.makedirs(directory, exist_ok=True)


# create crawled and queue file
def create_data_files(project_name, base_url):
    queue = project_name + '\\queue.txt'
    crawled = project_name + '\\crawled.txt'
    if not os.path.isfile(queue):
        write_file(queue, base_url)
    if not os.path.isfile(crawled):
        write_file(crawled, "")


# create new files
def write_file(path, data):
    with open(path,'w') as f:
        f.write(data)
        f.close()


# add data to an existing file
def append_to_file(path, data):
    with open(path, 'a') as file:
        file.write(data + "\n")
        file.close()


# detete the file data
def deleta_file_data(path):
    open(path, 'w').close()

# we will use set so that there is no repitition of data
# file to set
def file_to_set(file_name):
    result = set()
    with open(file_name, 'rt') as f:
        for line in f:
            result.add(line.replace('\n', ''))
    return result


# set to file every new line
def set_to_file(links, file):
    with open(file,'w') as f:
        for l in sorted(links):
            f.write(l+"\n")

