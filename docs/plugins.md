## Get Started With Plugins

Customize your labs to suit your teaching style and students' learning better! Create your own `labguide` plugin using Python and enable it just for your class.

### 1. Navigate to the Plugins Folder

Your plugin scripts should reside in the `.plugins` folder within your course's directory.

```
cd .plugins
```

### 2. Create Plugin Script

Create a new Python file inside the `.plugins` folder. The file should have a `.py` extension, and the name of the file will be used to reference the plugin.

Example: `.plugins/hello.py`

```
def hello():
    print("hello, world")
```

### 3. Define Plugin Functions

Each plugin should define functions that interact with LabGuide, customizing behavior based on your requirements. You can also define additional helper functions you want the plugin to use.

#### Key Considerations

- Naming: Use descriptive names for your functions so they clearly indicate their purpose.
- Parameters: Functions can take parameters, such as student results or lab data, to customize their behavior.
- Return Values: Functions can return values that LabGuide or other plugins may use.

### 4. Implementation

After writing the plugin, the final step is to enable it by including it in the lab's `.config.yml` file. This step will ensure the plugin is executed during lab sessions.

Add this section to the end of the `.config.yml` file.

```
### Code above not shown ###

plugins:
  - hello.py
  - another_plugin.py
  # - turnoff_plugin.py     Comment the line to turn off a specific plugin.
```

Note: Take note of the indentation, ensure that it is consistent throughout.
