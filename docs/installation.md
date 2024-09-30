**Note: You will be required to have permission and be authenticated before having access to the LabGuide of the courses.**

## Lab0

Lab0 is provided in this open source LabGuide. The `lab0` contains the following files:
- .config.yml
- .encrypted_lab0_solution
- requirements.txt
- lab0.ipynb

You can try out LabGuide's autograding feature by following the instructions in `lab0.ipynb`.

## Installation

Install LabGuide package
```
pip install git+https://github.com/suss-vli/labguide.git
```

### Initial Setup

Create a folder to store all the labs. Navigate to that folder and run the setup command.
```
cd <lab directory>
labguide setup
```
For example:
```
cd labs 
labguide setup
```

The setup will create a `lab0/` folder in your current working directory, and includes `lab0.ipynb` for you to try out.

### Setup for Courses

1. Navigate to the lab folder.

 
```
cd <lab directory>
```

2. To get the labs of the course and set up the LabGuide environment, you can use the command:

 
```
labguide get <course>
```
For example:
```
labguide get ict133
```
This command will `git clone` the course's labs into the `<course>/` folder.

3. Run the `setup` command:

 
```
labguide setup <course>
```
For example:
```
labguide setup ict133
```
This command will install all the dependencies required for the labs.

4. Your labs are now ready for you!

## Troubleshooting

#### 1. Permission Denied Error

Make sure you have been granted the necessary permissions to access the LabGuide repository or course materials. Reach out to the course administrator or repository owner to request access if necessary.

#### 2. Authentication Required Error

Key in the correct credentials when prompted by GitHub.

#### 3. LabGuide Command
If you are facing issues when running `labguide get <course>`, ensure you are using the correct course identifier and that the course is available in the repository. Double-check for typos or access restrictions on the course itself.
