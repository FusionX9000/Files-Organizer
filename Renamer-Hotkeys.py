import sys
import re
import os

def clean_numbered(filename):
    ext = ""
    if '.' in filename:
        ext = "."+getext(filename)
        filename = getfilename(filename)
    cleaned_filename = re.sub("\([^(^)]*\)", "", filename).strip()
    return cleaned_filename+ext

def getfilename(filename):
    if not '.' in filename: return filename
    return '.'.join(filename.split('.')[:-1])

def getext(filename):
    return filename.split('.')[-1]

def mergefileext(filename,ext):
    return '.'.join([filename,ext])

def rename(filename, title, source,destination):
    extension = getext(filename)
    tmp = title
    filelocation = os.path.join(destination, mergefileext(tmp,extension))
    c = 0
    while os.path.exists(filelocation):
        c += 1
        tmp=title + " ({})".format(str(c))
        filelocation = os.path.join(destination, mergefileext(tmp,extension))
    title = tmp
    command = "move \"%s\\%s\" \"%s\\%s\"" % (source, filename, destination, mergefileext(title,extension))
    # print(command)
    # os.system(command)
    os.rename(os.path.join(source, filename), os.path.join(destination, mergefileext(title,extension)))


def find_tags(filename,tag):
    tags = re.findall("\[[A-Za-z]\]", filename)
    if not tag in tags: tags+=tag.split()
    tags = sorted(tags, key=lambda k: k.replace('[', '').replace(']', ''))
    if '[N]' in tags:
        del tags[tags.index("[N]")]
        tags = ["[N]"] + tags
    if '[F]' in tags:
        del tags[tags.index("[F]")]
        tags = tags + ["[F]"]
    return ' '.join(tags)

def add_tags(arguments,tags):
    for x in arguments[1:]:
        split_x = x.split('\\')
        o_filename = split_x[-1]
        source = '\\'.join(split_x[:-1])
        new_tags = find_tags(o_filename,tags)
        tmp = clean_numbered(getfilename(o_filename)).split('[')[0].strip()
        title = "{} {}".format(tmp,new_tags)
        rename(o_filename,title,source,source)

def add_suffix(arguments,suffix):
    for x in arguments[1:]:
        split_x = x.split('\\')
        o_filename = split_x[-1]
        source = '\\'.join(split_x[:-1])
        tmp = clean_numbered(getfilename(o_filename)).strip()
        title = "{} - {}".format(suffix, tmp)
        rename(o_filename,title,source,source)

def run():
    arguments = [x.strip() for x in sys.argv[1:]]
    if not arguments: return
    arg1 = arguments[0]
    if '_' in arg1:
        suffix = arg1+"misc"
        add_suffix(arguments, suffix)
    else:
        tags = "[{}]".format(arg1)
        add_tags(arguments, tags)

if __name__ == "__main__":
    run()

