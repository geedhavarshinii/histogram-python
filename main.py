import yaml

if __name__ == '__main__':
    #loading the yaml file
    with open("histogram_code.yaml", "r") as file:
        yaml_data = yaml.safe_load(file)
    #executing the python code stored as 'code' in the yaml file
    exec(yaml_data['code'])
