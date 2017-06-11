import dotinstall.util.parser as parser
import dotinstall.dotinstall

if __name__ == "__main__":
    options = parser.parse_options(parser.read_options())
    dotinstall.main(options)
