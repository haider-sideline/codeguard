// TEST DATA ONLY - intentionally insecure JavaScript for scanner testing.
const AUTH_TOKEN = "test-token-abcdef123456";          // VULN-08: hard-coded token

function render(userInput) {
  document.getElementById("out").innerHTML = userInput; // VULN-09: XSS via innerHTML
}

function run(code) {
  return eval(code);                                    // VULN-10: eval
}

module.exports = { render, run, AUTH_TOKEN };
