"""
Adding a copy and paste button to the output of the solution & hint.
Using clipboardjs to copy the solution/hint to the clipboard. 
"""
from IPython.display import display, HTML

js = """
<input id="foobar" value="https://github.com/zenorocha/clipboard.js.git" />

<button class="copyBtn" data-clipboard-target="#foobar" onclick="copyToClipboard()">
  <img alt="Copy to clipboard" />
</button>

<script>
 function copyToClipboard() {
     console.log("attempting to copy...");
     var inputValue = document.getElementById("foobar").value;
     navigator.clipboard.writeText(inputValue);
 }
</script>
"""

# Display the JavaScript
display(HTML(js))
