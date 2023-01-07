import OFEngine

if __name__ == "__main__":

    ef = OFEngine.OFE_file("Marball", "/home/imam/Marball/")

    print(ef.name)
    print(ef.location)
    print(ef.path)
    print(ef.file)
    print(ef.size)
    print(ef.ck)
    print(ef.arch)
    print(ef.type)
    print(ef.stripped)
    print(ef.provide)
    print(ef.deps)
    print(ef.glibc_versions)
    print(ef.glibcxx_versions)
