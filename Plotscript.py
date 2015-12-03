import Groupby
import Generate
import Genplots
import CreateSchema
import sys

def main(argv):	
	CreateSchema.main(argv)	
	Generate.main("Schema.csv", "prototype.csv")
	Groupby.main(argv, "Schema.csv")
	Genplots.main(argv, "experiment.csv", "groups.csv")

if __name__ == '__main__':	
	main(sys.argv[1])
