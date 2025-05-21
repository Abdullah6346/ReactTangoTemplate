#!/usr/bin/env node

/**
 * Full Stack Framework Installer
 * TanStack Router + Django
 */
import { execSync } from "child_process";
import readline from "readline";
// ANSI color codes for terminal output
const colors = {
  green: "\x1b[32m",
  blue: "\x1b[34m",
  yellow: "\x1b[33m",
  red: "\x1b[31m",
  reset: "\x1b[0m",
};

// Print banner
console.log(`${colors.blue}=================================`);
console.log(`${colors.green}Full Stack Framework Installer`);
console.log(`${colors.blue}TanStack Router + Django`);
console.log(`${colors.blue}=================================${colors.reset}`);

/**
 * Check if a command exists
 * @param {string} command - Command to check
 * @returns {boolean} - Whether the command exists
 */
function commandExists(command) {
  try {
    execSync(`which ${command}`, { stdio: "ignore" });
    return true;
  } catch (e) {
    return false;
  }
}

/**
 * Execute a command and handle errors
 * @param {string} command - Command to execute
 * @param {string} errorMessage - Error message to display if the command fails
 */
function executeCommand(command, errorMessage) {
  try {
    console.log(`Executing: ${command}`);
    execSync(command, { stdio: "inherit" });
  } catch (error) {
    console.error(`${colors.red}${errorMessage}${colors.reset}`);
    console.error(error.message);
    process.exit(1);
  }
}

/**
 * Install backend dependencies
 * @param {Object} options - Installation options
 */
function installBackend(options) {
  console.log(
    `\n${colors.yellow}Installing backend (Django) dependencies...${colors.reset}`
  );

  // Check if Python is installed
  if (!commandExists("python3")) {
    console.error(
      `${colors.red}Python 3 is not installed. Please install Python 3 and try again.${colors.reset}`
    );
    process.exit(1);
  }

  // Check if pip is installed
  if (!commandExists("pip") && !commandExists("pip3")) {
    console.error(
      `${colors.red}pip is not installed. Please install pip and try again.${colors.reset}`
    );
    process.exit(1);
  }

  // Create and activate virtual environment (optional)
  if (options.useVenv) {
    console.log("Creating virtual environment...");
    executeCommand(
      "python3 -m venv venv",
      "Failed to create virtual environment."
    );

    // Detect OS for the correct activate command
    const isWindows = process.platform === "win32";
    const activateCommand = isWindows
      ? ".\\venv\\Scripts\\activate"
      : "source venv/bin/activate";
    console.log(`To activate the virtual environment, run: ${activateCommand}`);
  }

  // Install Python dependencies
  console.log("Installing Python packages from requirements.txt...");
  const pipCommand = commandExists("pip3") ? "pip3" : "pip";
  executeCommand(
    `${pipCommand} install -r requirements.txt`,
    "Failed to install Python dependencies."
  );

  console.log(
    `${colors.green}✓ Backend dependencies installed successfully${colors.reset}`
  );
}

/**
 * Install frontend dependencies
 */
function installFrontend() {
  console.log(
    `\n${colors.yellow}Installing frontend (React + TanStack Router) dependencies...${colors.reset}`
  );

  // Check if Node.js is installed
  if (!commandExists("node")) {
    console.error(
      `${colors.red}Node.js is not installed. Please install Node.js and try again.${colors.reset}`
    );
    process.exit(1);
  }

  // Check if pnpm is installed, if not try to install it
  if (!commandExists("pnpm")) {
    console.log("pnpm is not installed. Attempting to install pnpm...");
    if (commandExists("npm")) {
      executeCommand("npm install -g pnpm", "Failed to install pnpm.");
    } else {
      console.error(
        `${colors.red}npm is not installed. Please install npm or pnpm and try again.${colors.reset}`
      );
      process.exit(1);
    }
  }

  // Install Node.js dependencies
  console.log("Installing Node.js packages with pnpm...");
  executeCommand("pnpm install", "Failed to install Node.js dependencies.");

  console.log(
    `${colors.green}✓ Frontend dependencies installed successfully${colors.reset}`
  );
}

/**
 * Parse command-line arguments
 * @returns {Object} Options object
 */
function parseArguments() {
  const options = {
    installBackend: true,
    installFrontend: true,
    useVenv: false,
  };

  const args = process.argv.slice(2);

  for (let i = 0; i < args.length; i++) {
    const arg = args[i];

    switch (arg) {
      case "--backend-only":
        options.installFrontend = false;
        break;
      case "--frontend-only":
        options.installBackend = false;
        break;
      case "--with-venv":
        options.useVenv = true;
        break;
      case "--help":
        console.log("Usage: node install.js [options]");
        console.log("Options:");
        console.log("  --backend-only    Install only the Django backend");
        console.log("  --frontend-only   Install only the React frontend");
        console.log(
          "  --with-venv       Create and use a Python virtual environment"
        );
        console.log("  --help            Show this help message");
        process.exit(0);
        break;
      default:
        console.error(`Unknown parameter: ${arg}`);
        process.exit(1);
    }
  }

  return options;
}

/**
 * Main installation function
 */
async function main() {
  const options = parseArguments();

  // Display installation plan
  console.log(`\n${colors.blue}Installation Plan:${colors.reset}`);
  if (options.installBackend) {
    console.log("- Backend (Django)");
  }
  if (options.installFrontend) {
    console.log("- Frontend (React + TanStack Router)");
  }

  // Ask for confirmation
  const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
  });

  const answer = await new Promise((resolve) => {
    rl.question("Proceed with installation? (y/n): ", resolve);
  });

  rl.close();

  if (answer.toLowerCase() !== "y" && answer.toLowerCase() !== "yes") {
    console.log("Installation cancelled.");
    process.exit(0);
  }

  // Run installations
  if (options.installBackend) {
    installBackend(options);
  }

  if (options.installFrontend) {
    installFrontend();
  }

  // Final message
  console.log(
    `\n${colors.green}Installation completed successfully!${colors.reset}`
  );
  console.log(
    `${colors.blue}To start the development server, run:${colors.reset}`
  );
  console.log(`  ${colors.yellow}pnpm run dev${colors.reset}`);

  // If using virtual environment, remind user
  if (options.useVenv) {
    const isWindows = process.platform === "win32";
    const activateCommand = isWindows
      ? ".\\venv\\Scripts\\activate"
      : "source venv/bin/activate";

    console.log(
      `\n${colors.yellow}Note:${colors.reset} You're using a Python virtual environment.`
    );
    console.log(`To activate it in the future, run: ${activateCommand}`);
  }
}

// Run the main function
main().catch((error) => {
  console.error(`${colors.red}Installation failed:${colors.reset}`, error);
  process.exit(1);
});
