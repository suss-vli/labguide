# Sysadmin Guide

## Deploying `labguide` to virtual environments

When setting up `labguide` for virtual environments like Vocareum, or built within a Docker image, directly `pip install` and running the `labguide get` command will not work due to the need for authentication. 

Hence, you will need to follow a different set of steps to set up `labguide`. 

The commands will ensure that `.plugins` folder is available and course labs are added to the environment.

 
The commands apply to all courses:
- ICT133
- ICT162
- ICT233 (as of now, no `.unencrypted_ict233_solution` in the repo yet)
- ANL588 (as of now, no `.unencrypted_ict233_solution` in the repo yet)

### Commands to set up `labguide`

```
pip3 install git+https://github.com/suss-vli/labguide.git
labguide setup
rm -rf lab0/
git clone https://username:{PAT}@github.com/suss-vli/labguide_<course>
cd labguide_<course>
rm -rf .unencrypted_<course>_solution
```
Replace `<course>` for the course code that you are setting up for, e.g. `ict133`.

Replace `username` and `PAT` with your Github username and PAT. 
 

### Optional Steps

The following are optional steps:

- If you wish to move the labs out to desktop, you can move the labs in any commands after.

- Hiding or moving `.encrypted_<course>_solution/` to a different directory as labs:
    - `mv .encrypted_<course>_solution <new location>`
    
    - Ensure you have an updated `.config.yml` with the new folder location for `suss_path`. 
    
        `COPY .config.yml` to replace the existing `.config.yml` in the `labguide_<course>` directory.

 
If there is no need to hide away the `.encrypted_<course>_solution` folder, you dont have to `mv` the solution folder or `COPY` the config file.
