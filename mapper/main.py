"""Cloud mapper - visualize the network flow of resources on the configured aws profile and region"""

import cli

def main():
    args = cli.parse_args()
    regions = determine_regions( args )
    region_data = fetch_resources( regions )
    generate_dot_files( region_data,output_file )

def determine_regions():
    pass

def fetch_resources():
    pass

def generate_dot_files():
    pass

if __name__ == "__main__":
    main()