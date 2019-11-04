import sys

rental_columns = ['pid', 'hid', 'pn', 's', 'hs', 'hz', 'hc']
boat_columns = ['bl', 'bno', 'z', 't', 'bn', 'ssn']

if __name__ == "__main__":
    table = sys.argv[1]
    with open("test.sql", "w") as this_file:
        if table == 'rentals':
            for column1 in rental_columns:
                for column2 in rental_columns:
                    this_file.write(f"select '{table}:{column1} --> {column2}' as fd,\ncase when count(*) = 0 then 'may hold' \nelse 'does not hold' end as validity from \n\t(select t.{column1} \n\tfrom {table} t \n\tgroup by t.{column1}\n\t having count(distinct t.{column2}) > 1\n\t) X;\n\n")
        else:
            for column1 in boat_columns:
                for column2 in boat_columns:
                    this_file.write(f"select '{table}:{column1} --> {column2}' as fd,\ncase when count(*) = 0 then 'may hold' \nelse 'does not hold' end as validity from \n\t(select t.{column1} \n\tfrom {table} t \n\tgroup by t.{column1}\n\t having count(distinct t.{column2}) > 1\n\t) X;\n\n")
