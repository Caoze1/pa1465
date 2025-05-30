import pandas as pd
import json

VERSIONS = ("3.8", "3.10", "3.12")
OSS = ("Windows", "Linux", "Darwin")
COLORS = {"g":"green!30", "o":"orange!40", "r":"red!40", "w":"white!30"}

def extract_results(tname, test_dict, pyver, os, test_hashes):
    rlist = []
    for key, entry in test_dict.items():
        if key == "info":
            continue
        if pyver in entry['py_ver'] and os in entry['platform']:
            rlist.append(entry)

    if len(rlist) < 0:
        print(f"Not enough entry for test: {tname}, py: {pyver}, os: {os}")
        test_hashes.append("-")
        test_hashes.append("-")
        return
    
    h0 = rlist[0]['hash']
    h1 = rlist[1]['hash']
    test_hashes.append(h0)
    test_hashes.append(h1)

def export_table(data, suite):
    table = ""
    table += "\\begin{table}[H]"
    table += "\\scriptsize"
    table += "\\begin{tabular}{l|lll|lll|lll|l|}"
    table += "\\cline{2-11}"
    table += "& \\multicolumn{3}{c|}{\\textbf{Windows}}"
    table += "& \\multicolumn{3}{c|}{\\textbf{Linux}}"
    table += "& \\multicolumn{3}{c|}{\\textbf{Mac OS}}"
    table += "& \\textbf{Pass} \\\\ \\hline"

    table += "\\multicolumn{1}{|c|}{\\textbf{Python version}}"
    table += "& \\multicolumn{1}{c|}{\\textbf{"+VERSIONS[0]+"}}"
    table += "& \\multicolumn{1}{c|}{\\textbf{"+ VERSIONS[1] +"}} & \\textbf{"+VERSIONS[2]+"}"
    table += "& \\multicolumn{1}{c|}{\\textbf{"+VERSIONS[0]+"}}"
    table += "& \\multicolumn{1}{c|}{\\textbf{"+VERSIONS[1]+"}} & \\textbf{"+VERSIONS[2]+"}"
    table += "& \\multicolumn{1}{c|}{\\textbf{"+VERSIONS[0]+"}}"
    table += "& \\multicolumn{1}{c|}{\\textbf{"+VERSIONS[1]+"}} & \\textbf{"+VERSIONS[2]+"} & \\\\ \\hline"
    for test in data:
        if test[2] != suite:
            continue
        table += "\\multicolumn{1}{|l|}{"+ test[0] + "}"

        for cell in test[1]:
            table += "& \\multicolumn{1}{c|}{\\cellcolor{" + COLORS[cell[1]] + "}" + cell[0] + "}\n"

        table += "\\\\ \\hline"
        table += "\n"

    table += "\\end{tabular}\n"
    table += "\\caption{Traceability Matrix for test suite " + str(suite) + "}\n"
    table += "\\label{tab:matrix" + str(suite) + "}\n"
    table += "\\end{table}\n"

    return table
    # filename = "ltx"+str(suite)+".txt"
    # with open(filename, "w") as file:
    #     file.write(table)

def main():
    table_results = []
    with open("test_results.json", "r") as file:
        results = json.load(file)

    ### Iterate over each test
    for test_name, test_dict in results.items():
        test_hashes = []
        test_suite = test_dict["info"]["test_suite"]

        ### Get hash results for os/python combinations
        for os_i in range(3):
            for pyver_i in range(3):
                extract_results(test_name, test_dict, VERSIONS[pyver_i], OSS[os_i], test_hashes)
        
        num = 1
        hash_dict = {}
        test_row = []

        ### Compare each os/py combination
        for i in range(0, len(test_hashes), 2):
            run0 = test_hashes[i]
            run1 = test_hashes[i+1]
            
            # No result
            if run0 == "-" or run1 == "-":
                test_row.append(("-","w"))
                continue

            cell = ""
            color = "g"
            if run0 in hash_dict:
                cell += str(hash_dict[run0])
            else:
                # New result
                hash_dict[run0] = num
                cell += str(num)
                num += 1

            if hash_dict[run0] != 1:
                # Different hashes
                color = "o"
            
            if run0 != run1:
                # Different hashes with same os and python version
                color = "r"
                if run1 in hash_dict:
                    cell += "/" + str(hash_dict[run1])
                else:
                    hash_dict[run1] = num
                    cell += "/"+str(num)
                    num += 1
            test_row.append((cell, color))

        # Add pass
        if len(hash_dict) == 1:
            test_row.append(("Yes", "g"))
        else:
            test_row.append(("No", "r"))
        
        table_results.append((test_name, test_row, test_suite))
    
    tables = [export_table(table_results, 1), export_table(table_results, 2), export_table(table_results, 3), export_table(table_results, 4)]
    total = tables[0] + "\n\n" + tables[1] + "\n\n" + tables[2] + "\n\n" + tables[3]

    filename = "ltx.txt"
    with open(filename, "w") as file:
        file.write(total)
    
    for i in range(1,5):
        filename = "ltx"+ str(i) +".txt"
        with open(filename, "w") as file:
            file.write(tables[i-1])

if __name__=='__main__':
    main()
