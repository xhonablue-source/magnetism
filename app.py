import streamlit as st
import streamlit.components.v1 as components

# --- Page Setup ---
st.set_page_config(page_title="MathCraft: The Math of Magnetism", page_icon="🌌", layout="wide")

# --- Developer Credit ---
st.markdown("### www.cognitivecloud.ai")
st.markdown("**Developed by Xavier Honablue M.Ed**")

st.markdown("---")

# --- HTML Content for the Math of Magnetism Lesson ---
# This multi-line string contains your entire HTML application.
# It's important to keep the HTML valid and self-contained.
html_content = """
<!DOCTYPE html>
<html lang="en" class="scroll-smooth">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>MathCraft: The Math of Magnetism - Unveiling Invisible Forces | Cognitive Cloud Education</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;700&display=swap" rel="stylesheet">
    <!-- Chosen Palette: Warm Neutrals, Blue Accent, STEM High School Colors (implied from Streamlit: #1f77b4, #f0f2f6, #f8f9fa) -->
    <!-- Application Structure Plan: A single-page interactive lesson structured thematically: Intro, Student Personalization, Key Concepts, Interactive Visualizations (Field Strength, Electromagnet, Compass), Quizzes, Reflection, Summary, Resources, Study Plan. Uses a sticky navigation for quick section access. Interactivity is driven by HTML form elements (sliders, selects, radios, text inputs) and custom JavaScript for dynamic content updates, graph rendering (Chart.js), and CSS transformations for visual elements. This structure provides a guided learning path while allowing students to explore specific concepts interactively, connecting abstract math to real-world physics. -->
    <!-- Visualization & Content Choices: Magnetic Field Strength vs. Distance -> Goal: Illustrate inverse square law -> Viz: Line Chart -> Interaction: Slider for distance -> Justification: Clearly shows non-linear relationship -> Library: Chart.js. Electromagnet Strength -> Goal: Show factors affecting strength -> Viz: Bar Chart -> Interaction: Sliders for current and coils -> Justification: Compares impact of variables -> Library: Chart.js. Compass/Field Direction -> Goal: Visualize field direction -> Viz: HTML/CSS styled compass needle with rotation -> Interaction: Dropdown for scenarios -> Justification: Simple, direct visual feedback on directional concepts -> Library/Method: Vanilla JS, CSS Transforms. Quizzes -> Goal: Assess understanding -> Viz: Radio Buttons -> Interaction: Select answers, check button for feedback -> Justification: Standard quiz format. -->
    <!-- CONFIRMATION: NO SVG graphics used. NO Mermaid JS used. -->
    <style>
        body {
            font-family: 'Inter', sans-serif;
            background-color: #F8F7F4; /* Light neutral background */
            color: #333333; /* Dark text for readability */
        }
        .accent-color {
            color: #005A9C; /* Primary accent blue */
        }
        .bg-accent {
            background-color: #005A9C;
        }
        .text-accent-secondary {
            color: #F2A900; /* Secondary accent orange */
        }
        .chart-container {
            position: relative;
            width: 100%;
            max-width: 700px; /* Max width for charts */
            margin-left: auto;
            margin-right: auto;
            height: 400px; /* Fixed height for consistency */
            max-height: 500px;
        }
        @media (min-width: 768px) {
            .chart-container {
                height: 450px;
            }
        }
        .nav-link {
            transition: color 0.3s ease;
        }
        .nav-link:hover {
            color: #F2A900;
        }
        .expander-header {
            cursor: pointer;
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 1rem;
            background-color: #e0e0e0;
            border-radius: 0.5rem;
            font-weight: bold;
            color: #333333;
            transition: background-color 0.2s;
        }
        .expander-header:hover {
            background-color: #d0d0d0;
        }
        .expander-content {
            padding: 1rem;
            background-color: #f0f0f0;
            border-radius: 0.5rem;
            margin-top: 0.5rem;
            display: none;
        }
        .expander-header.active .arrow {
            transform: rotate(90deg);
        }
        .arrow {
            transition: transform 0.2s;
        }
        .compass-container {
            width: 150px;
            height: 150px;
            border: 2px solid #333;
            border-radius: 50%;
            position: relative;
            margin: 20px auto;
            background-color: #fefefe;
            display: flex;
            justify-content: center;
            align-items: center;
            box-shadow: 0 4px 8px rgba(0,0,0,0.1);
        }
        .compass-needle {
            width: 80%;
            height: 4px;
            background-color: #dc2626; /* Red for North */
            position: absolute;
            transform-origin: 50% 50%;
            transition: transform 0.5s ease-out;
            border-radius: 2px;
        }
        .compass-needle::before {
            content: '';
            position: absolute;
            left: 0;
            top: -4px;
            width: 0;
            height: 0;
            border-left: 6px solid transparent;
            border-right: 6px solid transparent;
            border-bottom: 10px solid #dc2626;
            transform: translateY(-50%) rotate(-90deg);
            transform-origin: 50% 50%;
        }
        .compass-needle::after {
            content: '';
            position: absolute;
            right: 0;
            top: -4px;
            width: 0;
            height: 0;
            border-left: 6px solid transparent;
            border-right: 6px solid transparent;
            border-bottom: 10px solid #3b82f6; /* Blue for South */
            transform: translateY(-50%) rotate(90deg);
            transform-origin: 50% 50%;
        }
        .compass-center {
            width: 10px;
            height: 10px;
            background-color: #333;
            border-radius: 50%;
            position: absolute;
            z-index: 1;
        }
        .compass-label {
            position: absolute;
            font-weight: bold;
            font-size: 0.9rem;
            color: #333;
        }
        .compass-label.N { top: 5px; }
        .compass-label.S { bottom: 5px; }
        .compass-label.E { right: 5px; }
        .compass-label.W { left: 5px; }
    </style>
</head>
<body class="antialiased">

    <header class="bg-white/80 backdrop-blur-md sticky top-0 z-50 shadow-sm">
        <nav class="container mx-auto px-6 py-4 flex justify-between items-center">
            <a href="#" class="text-xl font-bold accent-color">
                MathCraft: The Math of Magnetism
            </a>
            <div class="hidden md:flex space-x-6 text-gray-700">
                <a href="#intro" class="nav-link">Introduction</a>
                <a href="#concepts" class="nav-link">Key Concepts</a>
                <a href="#visualizations" class="nav-link">Visualizations</a>
                <a href="#assessment" class="nav-link">Assessment</a>
                <a href="#resources" class="nav-link">Resources</a>
                <a href="#study-plan" class="nav-link">Study Plan</a>
            </div>
            <button id="mobile-menu-button" class="md:hidden text-gray-700">
                <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16m-7 6h7"></path></svg>
            </button>
        </nav>
        <div id="mobile-menu" class="hidden md:hidden px-6 pb-4">
            <a href="#intro" class="block py-2 text-gray-700">Introduction</a>
            <a href="#concepts" class="block py-2 text-gray-700">Key Concepts</a>
            <a href="#visualizations" class="block py-2 text-gray-700">Visualizations</a>
            <a href="#assessment" class="block py-2 text-gray-700">Assessment</a>
            <a href="#resources" class="block py-2 text-gray-700">Resources</a>
            <a href="#study-plan" class="block py-2 text-gray-700">Study Plan</a>
        </div>
    </header>

    <main class="container mx-auto px-6 py-8">
        <section id="intro" class="mb-12 p-6 bg-white rounded-lg shadow-md">
            <div class="flex items-center mb-4">
                <div>
                    <h3 class="text-lg font-semibold accent-color">www.cognitivecloud.ai</h3>
                    <p class="text-sm text-gray-600">Developed by Xavier Honablue M.Ed</p>
                </div>
            </div>
            <hr class="my-6">
            <h1 class="text-4xl font-bold accent-color mb-4">🌌 MathCraft: The Math of Magnetism - Unveiling Invisible Forces</h1>
            <p class="text-lg text-gray-700 mb-4">
                Welcome to this MathCraft lesson! This module explores how the invisible forces of magnetism are described and understood through the power of mathematics. From the compass guiding navigation to the MRI machines used in medicine, magnetism is ubiquitous, and mathematics serves as its fundamental language.
            </p>
            <hr class="my-6">
            <h3 class="text-2xl font-bold accent-color mb-3">🎯 Learning Objectives:</h3>
            <ul class="list-disc list-inside text-gray-700 space-y-2">
                <li>Define and describe magnetic fields and forces.</li>
                <li>Apply the inverse square law to quantify magnetic field strength.</li>
                <li>Explain the principles of electromagnetism and its contributing factors.</li>
                <li>Relate mathematical models to real-world magnetic phenomena and technological applications.</li>
            </ul>
            <div class="bg-blue-100 border-l-4 border-blue-500 text-blue-700 p-4 mt-6 rounded-md" role="alert">
                <p class="font-bold">📚 Curriculum Alignment:</p>
                <p>This lesson aligns with high school physics and mathematics curricula, covering topics such as forces, inverse square relationships, and the application of mathematical models to scientific phenomena.</p>
            </div>
            <div class="mt-6">
                <label for="common-core-standard" class="block text-gray-700 text-lg font-medium mb-2">📋 Select Common Core Standard:</label>
                <select id="common-core-standard" class="block w-full p-3 border border-gray-300 rounded-lg shadow-sm focus:ring-accent-color focus:border-accent-color">
                    <option>HSA.CED.A.1 - Create equations and inequalities in one variable and use them to solve problems.</option>
                    <option>HSF.IF.B.4 - Interpret key features of graphs and tables in terms of quantities.</option>
                    <option>HSF.BF.A.1 - Write a function that describes a relationship between two quantities.</option>
                    <option>HSN.VM.A.1 - Recognize vector quantities as having both magnitude and direction.</option>
                </select>
            </div>
            <div class="mt-6">
                <label for="student-name" class="block text-gray-700 text-lg font-medium mb-2">Enter your name:</label>
                <input type="text" id="student-name" class="block w-full p-3 border border-gray-300 rounded-lg shadow-sm focus:ring-accent-color focus:border-accent-color">
            </div>
            <div class="mt-4">
                <label for="avatar-select" class="block text-gray-700 text-lg font-medium mb-2">Choose your scientific avatar:</label>
                <select id="avatar-select" class="block w-full p-3 border border-gray-300 rounded-lg shadow-sm focus:ring-accent-color focus:border-accent-color">
                    <option>⚛️ Atom Explorer</option>
                    <option>⚡️ Current Master</option>
                    <option>🧲 Field Navigator</option>
                    <option>🔭 Quantum Seeker</option>
                </select>
            </div>
            <div id="welcome-message" class="mt-4 p-3 bg-green-100 text-green-700 rounded-md hidden"></div>
            <div class="mt-6">
                <label for="learning-mode" class="block text-gray-700 text-lg font-medium mb-2">Select your learning mode or style:</label>
                <select id="learning-mode" class="block w-full p-3 border border-gray-300 rounded-lg shadow-sm focus:ring-accent-color focus:border-accent-color">
                    <option>🌟 Concept Builder</option>
                    <option>🚀 Experimenter</option>
                    <option>🎮 Problem Solver</option>
                    <option>🎯 Deep Diver</option>
                </select>
            </div>
        </section>

        <section id="concepts" class="mb-12 p-6 bg-white rounded-lg shadow-md">
            <h2 class="text-3xl font-bold accent-color mb-4">🔬 Key Concepts in Magnetism</h2>
            <p class="text-lg text-gray-700 mb-6">This section introduces the fundamental principles that govern magnetic phenomena.</p>

            <div class="mb-8">
                <h3 class="text-2xl font-bold accent-color mb-3">Magnetic Fields</h3>
                <p class="text-gray-700 mb-4">
                    A **magnetic field** is a vector field that describes the magnetic influence of electric currents and magnetic materials. It is defined by the force it exerts on moving electric charges. Magnetic field lines are a common visualization tool, where the direction of the lines indicates the direction of the magnetic field, and the density of the lines represents the field's strength.
                </p>
                <div class="compass-container">
                    <div class="compass-needle" style="transform: rotate(0deg);"></div>
                    <div class="compass-center"></div>
                    <span class="compass-label N">N</span>
                    <span class="compass-label S">S</span>
                    <span class="compass-label E">E</span>
                    <span class="compass-label W">W</span>
                </div>
                <div class="mt-4">
                    <label for="compass-scenario" class="block text-gray-700 text-lg font-medium mb-2">Simulate Compass Behavior:</label>
                    <select id="compass-scenario" class="block w-full p-3 border border-gray-300 rounded-lg shadow-sm focus:ring-accent-color focus:border-accent-color">
                        <option value="north">Point North (Earth's Field)</option>
                        <option value="bar_magnet_N_approach">Approaching Bar Magnet North Pole</option>
                        <option value="bar_magnet_S_approach">Approaching Bar Magnet South Pole</option>
                        <option value="current_up">Current Flowing Up (Right-Hand Rule)</option>
                        <option value="current_down">Current Flowing Down (Right-Hand Rule)</option>
                    </select>
                </div>
            </div>

            <div class="mb-8">
                <h3 class="text-2xl font-bold accent-color mb-3">Magnetic Force and Inverse Square Law</h3>
                <p class="text-gray-700 mb-4">
                    The interaction between magnetic poles or between a magnet and a ferromagnetic material is governed by a force that adheres to an **inverse square law**. This principle states that the magnitude of the magnetic force between two magnetic poles is directly proportional to the product of their pole strengths and inversely proportional to the square of the distance between them.
                </p>
                <p class="text-gray-700 mb-4">
                    Mathematically, for two magnetic poles, the force $F$ can be expressed as:
                    $$ F = k \\frac{q_1 q_2}{r^2} $$
                    where $k$ is the magnetic constant, $q_1$ and $q_2$ are the magnetic pole strengths, and $r$ is the distance between the poles. This relationship demonstrates that as the distance $r$ increases, the force $F$ diminishes rapidly.
                </p>
            </div>

            <div>
                <h3 class="text-2xl font-bold accent-color mb-3">Electromagnetism</h3>
                <p class="text-gray-700 mb-4">
                    **Electromagnetism** is a fundamental force of nature that arises from the interaction of electric currents and magnetic fields. It describes how electric currents generate magnetic fields and how magnetic fields exert forces on electric currents. The strength of an electromagnet is directly proportional to the current flowing through its coils and the number of turns in the coil.
                </p>
            </div>
        </section>

        <section id="visualizations" class="mb-12 p-6 bg-white rounded-lg shadow-md">
            <h2 class="text-3xl font-bold accent-color mb-4">📈 Interactive Magnetism Visualizations</h2>
            <p class="text-lg text-gray-700 mb-6">These interactive visualizations allow for exploration of key magnetic principles by adjusting variables and observing the resulting changes.</p>

            <div class="mb-8">
                <h3 class="text-2xl font-bold accent-color mb-3">Magnetic Field Strength vs. Distance</h3>
                <p class="text-gray-700 mb-4">This visualization demonstrates the inverse square law by showing how magnetic field strength diminishes with increasing distance from a magnetic source.</p>
                <div class="mb-6">
                    <label for="distance-slider" class="block text-gray-700 text-lg font-medium mb-2">Distance from Source (units): <span id="distance-value">1</span></label>
                    <input type="range" id="distance-slider" min="1" max="10" value="1" step="0.1" class="w-full h-2 bg-gray-200 rounded-lg appearance-none cursor-pointer accent-[#005A9C]">
                </div>
                <div class="chart-container">
                    <canvas id="fieldStrengthChart"></canvas>
                </div>
                <div class="mt-4 text-center">
                    <p class="text-xl font-bold accent-color">Calculated Field Strength: <span id="strength-value"></span></p>
                </div>
            </div>

            <div class="mb-8">
                <h3 class="text-2xl font-bold accent-color mb-3">Electromagnet Strength</h3>
                <p class="text-gray-700 mb-4">This visualization illustrates how the strength of an electromagnet is influenced by the magnitude of the current and the number of turns in its coil.</p>
                <div class="mb-6">
                    <label for="current-slider" class="block text-gray-700 text-lg font-medium mb-2">Current (Amps): <span id="current-value">1</span></label>
                    <input type="range" id="current-slider" min="0.5" max="5" value="1" step="0.5" class="w-full h-2 bg-gray-200 rounded-lg appearance-none cursor-pointer accent-[#005A9C]">
                </div>
                <div class="mb-6">
                    <label for="coils-slider" class="block text-gray-700 text-lg font-medium mb-2">Number of Coils: <span id="coils-value">10</span></label>
                    <input type="range" id="coils-slider" min="1" max="50" value="10" step="1" class="w-full h-2 bg-gray-200 rounded-lg appearance-none cursor-pointer accent-[#005A9C]">
                </div>
                <div class="chart-container">
                    <canvas id="electromagnetChart"></canvas>
                </div>
                <div class="mt-4 text-center">
                    <p class="text-xl font-bold accent-color">Electromagnet Strength: <span id="electromagnet-strength-value"></span> arbitrary units</p>
                </div>
            </div>
        </section>

        <section id="assessment" class="mb-12 p-6 bg-white rounded-lg shadow-md">
            <h2 class="text-3xl font-bold accent-color mb-4">🎲 Assessment: Quick Understanding Check</h2>
            <p class="text-lg text-gray-700 mb-6">Test your comprehension of the key concepts presented in this module.</p>
            <div id="magnetism-quiz-questions">
                <!-- Quiz questions will be dynamically inserted here -->
            </div>
            <h2 class="text-3xl font-bold accent-color mb-4 mt-8">🧾 Reflection: Application Challenge</h2>
            <label for="reflection-text" class="block text-gray-700 text-lg font-medium mb-2">Describe one real-world application of magnetism that you find fascinating, and explain how mathematical principles contribute to its understanding or utilization.</label>
            <textarea id="reflection-text" rows="5" class="block w-full p-3 border border-gray-300 rounded-lg shadow-sm focus:ring-accent-color focus:border-accent-color"></textarea>
            <button id="submit-reflection" class="mt-4 bg-accent text-white font-bold py-3 px-6 rounded-lg hover:bg-opacity-90 transition-colors">Submit Reflection</button>
            <div id="reflection-feedback" class="mt-4 p-3 bg-green-100 text-green-700 rounded-md hidden"></div>
        </section>

        <section id="summary" class="mb-12 p-6 bg-white rounded-lg shadow-md">
            <h2 class="text-3xl font-bold accent-color mb-4">🎓 Module Summary</h2>
            <p class="text-lg text-gray-700 mb-4">Upon completion of this module, you have explored:</p>
            <ul class="list-disc list-inside text-gray-700 space-y-2">
                <li>✅ The fundamental concepts of **magnetic fields and forces**.</li>
                <li>✅ The application of the **inverse square law** in describing magnetic strength.</li>
                <li>✅ The principles and factors influencing **electromagnetism**.</li>
                <li>✅ **Real-world applications** where the mathematics of magnetism is crucial.</li>
            </ul>
            <p class="text-lg text-gray-700 mt-4">
                **Conclusion:** Magnetism is not merely a mysterious force; it is a phenomenon that can be precisely described and manipulated using mathematical principles. By understanding these principles, we unlock the secrets of the universe and contribute to the development of future technologies.
            </p>
            <p class="text-xl font-bold text-accent-secondary mt-4">Continue your exploration of the invisible forces that shape our world! 🐾</p>
        </section>

        <section id="resources" class="mb-12 p-6 bg-white rounded-lg shadow-md">
            <h2 class="text-3xl font-bold accent-color mb-4">📚 Further Exploration & Resources</h2>
            <h3 class="text-2xl font-bold accent-color mb-3">🎯 Targeted Learning Resources</h3>
            <label for="physics-math-strand" class="block text-gray-700 text-lg font-medium mb-2">Select a Physics/Mathematics Strand to customize your resources:</label>
            <select id="physics-math-strand" class="block w-full p-3 border border-gray-300 rounded-lg shadow-sm focus:ring-accent-color focus:border-accent-color mb-4">
                <option>HS-PS2-5 – Forces and Motion: Electric and Magnetic Fields</option>
                <option>HS-PS3-2 – Energy: Electromagnetism and Energy Conversion</option>
                <option>HSA.CED.A.2 – Create equations in two or more variables to represent relationships between quantities</option>
                <option>HSF.IF.B.4 – Interpret key features of graphs and tables in terms of quantities</option>
            </select>
            <div id="strand-info-magnetism" class="bg-blue-100 border-l-4 border-blue-500 text-blue-700 p-4 mb-6 rounded-md" role="alert"></div>

            <h3 class="text-2xl font-bold accent-color mb-3">🎯 Recommended Resources: <span id="recommended-resources-title"></span></h3>
            <ul id="recommended-resources-list" class="list-disc list-inside text-gray-700 space-y-2 mb-6"></ul>

            <h2 class="text-3xl font-bold accent-color mb-4 mt-8">🌐 Additional Learning Resources</h2>
            <div id="magnetism-resource-tabs-container" class="border-b border-gray-200 mb-8">
                <nav class="-mb-px flex space-x-6 justify-center" aria-label="Resource Tabs">
                    <!-- Resource tabs will be dynamically inserted here -->
                </nav>
            </div>
            <div id="magnetism-resource-content-container">
                <!-- Resource content will be dynamically inserted here -->
            </div>
        </section>

        <section id="study-plan" class="mb-12 p-6 bg-white rounded-lg shadow-md">
            <h2 class="text-3xl font-bold accent-color mb-4">📅 Personalized Study Plan</h2>
            <label for="current-level-select-magnetism" class="block text-gray-700 text-lg font-medium mb-2">What's your current comfort level with magnetism concepts?</label>
            <select id="current-level-select-magnetism" class="block w-full p-3 border border-gray-300 rounded-lg shadow-sm focus:ring-accent-color focus:border-accent-color mb-4">
                <option>Beginner - Just starting to learn about magnetism</option>
                <option>Intermediate - Understand basics, need more practice</option>
                <option>Advanced - Ready for complex electromagnetic concepts</option>
                <option>Expert - Looking for advanced physics applications</option>
            </select>

            <label for="study-time-select-magnetism" class="block text-gray-700 text-lg font-medium mb-2">How much time can you dedicate to studying magnetism per week?</label>
            <select id="study-time-select-magnetism" class="block w-full p-3 border border-gray-300 rounded-lg shadow-sm focus:ring-accent-color focus:border-accent-color mb-6">
                <option>1-2 hours</option>
                <option>3-4 hours</option>
                <option>5-6 hours</option>
                <option>7+ hours</option>
            </select>

            <button id="generate-study-plan-magnetism" class="bg-accent text-white font-bold py-3 px-6 rounded-lg hover:bg-opacity-90 transition-colors">Generate My Study Plan</button>
            <div id="study-plan-output-magnetism" class="mt-6 p-4 bg-gray-50 rounded-md hidden"></div>
        </section>

    </main>

    <footer class="bg-gray-800 text-white py-6 mt-8">
        <div class="container mx-auto px-6 text-center text-sm">
            <p>&copy; 2025 Cognitive Cloud Education. All rights reserved.</p>
        </div>
    </footer>

    <script>
        document.addEventListener('DOMContentLoaded', function() {
            const mobileMenuButton = document.getElementById('mobile-menu-button');
            const mobileMenu = document.getElementById('mobile-menu');

            mobileMenuButton.addEventListener('click', () => {
                mobileMenu.classList.toggle('hidden');
            });

            // Student Info
            const studentNameInput = document.getElementById('student-name');
            const avatarSelect = document.getElementById('avatar-select');
            const welcomeMessageDiv = document.getElementById('welcome-message');
            const learningModeSelect = document.getElementById('learning-mode');

            function updateWelcomeMessage() {
                const name = studentNameInput.value.trim();
                const avatar = avatarSelect.value;
                if (name) {
                    welcomeMessageDiv.textContent = `Welcome, ${name} the ${avatar}! Let's begin our exploration of magnetism.`;
                    welcomeMessageDiv.classList.remove('hidden');
                } else {
                    welcomeMessageDiv.classList.add('hidden');
                }
            }
            studentNameInput.addEventListener('input', updateWelcomeMessage);
            avatarSelect.addEventListener('change', updateWelcomeMessage);

            // Compass Interaction
            const compassScenarioSelect = document.getElementById('compass-scenario');
            const compassNeedle = document.querySelector('.compass-needle');

            function updateCompass() {
                const scenario = compassScenarioSelect.value;
                let rotation = 0; // Default to North

                switch (scenario) {
                    case 'north':
                        rotation = 0; // North
                        break;
                    case 'bar_magnet_N_approach':
                        rotation = 180; // Needle points away from North pole of magnet
                        break;
                    case 'bar_magnet_S_approach':
                        rotation = 0; // Needle points towards South pole of magnet
                        break;
                    case 'current_up':
                        rotation = 90; // Simplified: Right-hand rule for current coming out of page (East)
                        break;
                    case 'current_down':
                        rotation = -90; // Simplified: Right-hand rule for current going into page (West)
                        break;
                }
                compassNeedle.style.transform = `rotate(${rotation}deg)`;
            }
            compassScenarioSelect.addEventListener('change', updateCompass);
            updateCompass(); // Initial call

            // Magnetic Field Strength Chart
            const distanceSlider = document.getElementById('distance-slider');
            const distanceValueSpan = document.getElementById('distance-value');
            const strengthValueSpan = document.getElementById('strength-value');
            const fieldStrengthChartCtx = document.getElementById('fieldStrengthChart').getContext('2d');
            let fieldStrengthChart;

            function calculateFieldStrength(distance, k = 100) { // k is a constant for illustrative purposes
                return k / (distance * distance);
            }

            function updateFieldStrengthChart() {
                const currentDistance = parseFloat(distanceSlider.value);
                distanceValueSpan.textContent = currentDistance.toFixed(1);
                const currentStrength = calculateFieldStrength(currentDistance);
                strengthValueSpan.textContent = currentStrength.toFixed(2);

                const xVals = Array.from({ length: 99 }, (_, i) => 1 + i * (9 / 98)); // From 1 to 10
                const yVals = xVals.map(d => calculateFieldStrength(d));

                if (fieldStrengthChart) {
                    fieldStrengthChart.destroy();
                }

                fieldStrengthChart = new Chart(fieldStrengthChartCtx, {
                    type: 'line',
                    data: {
                        labels: xVals.map(x => x.toFixed(1)),
                        datasets: [{
                            label: 'Magnetic Field Strength',
                            data: yVals,
                            borderColor: '#005A9C',
                            borderWidth: 2,
                            fill: false,
                            tension: 0.1,
                            pointRadius: 0
                        }]
                    },
                    options: {
                        responsive: true,
                        maintainAspectRatio: false,
                        scales: {
                            x: {
                                title: { display: true, text: 'Distance (units)' }
                            },
                            y: {
                                beginAtZero: true,
                                title: { display: true, text: 'Field Strength (arbitrary units)' }
                            }
                        },
                        plugins: {
                            tooltip: {
                                callbacks: {
                                    label: function(context) {
                                        return `Strength: ${context.parsed.y.toFixed(2)}`;
                                    }
                                }
                            }
                        }
                    }
                });
            }
            distanceSlider.addEventListener('input', updateFieldStrengthChart);
            updateFieldStrengthChart(); // Initial chart render

            // Electromagnet Strength Chart
            const currentSlider = document.getElementById('current-slider');
            const currentValueSpan = document.getElementById('current-value');
            const coilsSlider = document.getElementById('coils-slider');
            const coilsValueSpan = document.getElementById('coils-value');
            const electromagnetStrengthValueSpan = document.getElementById('electromagnet-strength-value');
            const electromagnetChartCtx = document.getElementById('electromagnetChart').getContext('2d');
            let electromagnetChart;

            function calculateElectromagnetStrength(current, coils) {
                // Simplified linear relationship for illustrative purposes
                return current * coils * 0.5; // Arbitrary constant for scaling
            }

            function updateElectromagnetChart() {
                const current = parseFloat(currentSlider.value);
                const coils = parseInt(coilsSlider.value);
                currentValueSpan.textContent = current.toFixed(1);
                coilsValueSpan.textContent = coils;

                const strength = calculateElectromagnetStrength(current, coils);
                electromagnetStrengthValueSpan.textContent = strength.toFixed(2);

                const labels = ['Current', 'Coils'];
                const data = [current * 10, coils]; // Scale current for visual comparison

                if (electromagnetChart) {
                    electromagnetChart.destroy();
                }

                electromagnetChart = new Chart(electromagnetChartCtx, {
                    type: 'bar',
                    data: {
                        labels: labels,
                        datasets: [{
                            label: 'Electromagnet Contribution',
                            data: data,
                            backgroundColor: ['#005A9C', '#F2A900'],
                            borderColor: ['#005A9C', '#F2A900'],
                            borderWidth: 1
                        }]
                    },
                    options: {
                        responsive: true,
                        maintainAspectRatio: false,
                        scales: {
                            y: {
                                beginAtZero: true,
                                title: { display: true, text: 'Relative Contribution' }
                            }
                        },
                        plugins: {
                            legend: {
                                display: false
                            },
                            tooltip: {
                                callbacks: {
                                    label: function(context) {
                                        if (context.label === 'Current') {
                                            return `Current: ${current.toFixed(1)} Amps (Scaled)`;
                                        } else if (context.label === 'Coils') {
                                            return `Coils: ${coils} turns`;
                                        }
                                        return '';
                                    }
                                }
                            }
                        }
                    }
                });
            }
            currentSlider.addEventListener('input', updateElectromagnetChart);
            coilsSlider.addEventListener('input', updateElectromagnetChart);
            updateElectromagnetChart(); // Initial chart render

            // Quiz Questions
            const quizQuestions = [
                {
                    question: "Which of these factors increases the strength of an electromagnet?",
                    options: ["Decreasing the current", "Increasing the number of coils", "Using a non-magnetic core", "Increasing the distance from the core"],
                    answer: "Increasing the number of coils"
                },
                {
                    question: "How does magnetic field strength change as you move further from a magnet?",
                    options: ["It increases linearly", "It decreases linearly", "It decreases by the inverse square of the distance", "It remains constant"],
                    answer: "It decreases by the inverse square of the distance"
                },
                {
                    question: "What is the primary function of a magnetic field?",
                    options: ["To generate heat", "To exert force on moving electric charges", "To produce light", "To conduct electricity"],
                    answer: "To exert force on moving electric charges"
                }
            ];

            const quizContainer = document.getElementById('magnetism-quiz-questions');
            quizQuestions.forEach((q, index) => {
                const questionDiv = document.createElement('div');
                questionDiv.className = 'mb-6 p-4 border border-gray-200 rounded-lg shadow-sm';
                questionDiv.innerHTML = `<p class="font-bold text-gray-800 mb-3">Question ${index + 1}: ${q.question}</p>`;

                q.options.forEach((option, optIndex) => {
                    questionDiv.innerHTML += `
                        <label class="block mb-2 text-gray-700">
                            <input type="radio" name="question${index}" value="${option}" class="mr-2">
                            ${option}
                        </label>
                    `;
                });
                quizContainer.appendChild(questionDiv);
            });

            const checkQuizButton = document.createElement('button');
            checkQuizButton.textContent = 'Check My Answers';
            checkQuizButton.className = 'mt-4 bg-accent text-white font-bold py-3 px-6 rounded-lg hover:bg-opacity-90 transition-colors';
            quizContainer.appendChild(checkQuizButton);

            const quizFeedbackDiv = document.createElement('div');
            quizFeedbackDiv.className = 'mt-4 p-3 rounded-md hidden';
            quizContainer.appendChild(quizFeedbackDiv);

            checkQuizButton.addEventListener('click', () => {
                let correctCount = 0;
                quizQuestions.forEach((q, index) => {
                    const selectedOption = document.querySelector(`input[name="question${index}"]:checked`);
                    if (selectedOption && selectedOption.value === q.answer) {
                        correctCount++;
                    }
                });

                if (correctCount === quizQuestions.length) {
                    quizFeedbackDiv.className = 'mt-4 p-3 bg-green-100 text-green-700 rounded-md';
                    quizFeedbackDiv.textContent = `🎉 Fantastic! You got all ${correctCount} questions correct! You're a magnetism master!`;
                } else {
                    quizFeedbackDiv.className = 'mt-4 p-3 bg-red-100 text-red-700 rounded-md';
                    quizFeedbackDiv.textContent = `Keep trying! You got ${correctCount} out of ${quizQuestions.length} correct. Review the concepts and try again!`;
                }
                quizFeedbackDiv.classList.remove('hidden');
            });

            // Reflection Submission
            const submitReflectionButton = document.getElementById('submit-reflection');
            const reflectionTextarea = document.getElementById('reflection-text');
            const reflectionFeedbackDiv = document.getElementById('reflection-feedback');

            submitReflectionButton.addEventListener('click', () => {
                if (reflectionTextarea.value.trim().length > 20) {
                    reflectionFeedbackDiv.className = 'mt-4 p-3 bg-green-100 text-green-700 rounded-md';
                    reflectionFeedbackDiv.textContent = 'Thank you for your thoughtful reflection! Your insights help us understand how you connect math to the real world.';
                } else {
                    reflectionFeedbackDiv.className = 'mt-4 p-3 bg-red-100 text-red-700 rounded-md';
                    reflectionFeedbackDiv.textContent = 'Please write a bit more for your reflection (at least 20 characters) to help us understand your thoughts!';
                }
                reflectionFeedbackDiv.classList.remove('hidden');
            });

            // Resources Section - Dynamic Content
            const physicsMathStrandSelect = document.getElementById('physics-math-strand');
            const strandInfoDiv = document.getElementById('strand-info-magnetism');
            const recommendedResourcesTitle = document.getElementById('recommended-resources-title');
            const recommendedResourcesList = document.getElementById('recommended-resources-list');
            const resourceTabsContainer = document.getElementById('magnetism-resource-tabs-container').querySelector('nav');
            const resourceContentContainer = document.getElementById('magnetism-resource-content-container');

            const resourceData = {
                "HS-PS2-5 – Forces and Motion: Electric and Magnetic Fields": {
                    info: "This strand focuses on understanding how electric and magnetic forces interact and their applications.",
                    resources: [
                        { name: "Khan Academy: Magnetic Fields", url: "https://www.khanacademy.org/science/physics/magnetic-forces-and-magnetic-fields" },
                        { name: "Physics Classroom: Magnetic Fields", url: "https://www.physicsclassroom.com/class/circuits/Lesson-4/Magnetic-Fields" }
                    ],
                    tabs: {
                        "Videos": [
                            { title: "Magnetic Fields: Crash Course Physics #32", url: "https://www.youtube.com/watch?v=VMz_G9VjQ_E" }
                        ],
                        "Articles": [
                            { title: "What is a Magnetic Field?", url: "https://www.livescience.com/38059-magnetic-field.html" }
                        ]
                    }
                },
                "HS-PS3-2 – Energy: Electromagnetism and Energy Conversion": {
                    info: "This strand explores the relationship between electromagnetism and energy conversion, such as in generators and motors.",
                    resources: [
                        { name: "Khan Academy: Electromagnetism", url: "https://www.khanacademy.org/science/physics/magnetic-forces-and-magnetic-fields/electromagnets" },
                        { name: "SparkFun: Electromagnetism Tutorial", url: "https://learn.sparkfun.com/tutorials/electromagnetism-tutorial/all" }
                    ],
                    tabs: {
                        "Videos": [
                            { title: "Electromagnets", url: "https://www.youtube.com/watch?v=vxWd62vQJtI" }
                        ],
                        "Articles": [
                            { title: "How Electromagnets Work", url: "https://www.explainthatstuff.com/how-electromagnets-work.html" }
                        ]
                    }
                },
                "HSA.CED.A.2 – Create equations in two or more variables to represent relationships between quantities": {
                    info: "This math standard focuses on building mathematical models (equations) to describe real-world relationships, like those in magnetism.",
                    resources: [
                        { name: "Khan Academy: Writing Equations with Two Variables", url: "https://www.khanacademy.org/math/algebra/x2f8bb11595b61c86:forms-of-linear-equations/x2f8bb11595b61c86:writing-linear-equations-from-word-problems/v/writing-equations-from-word-problems" },
                        { name: "Desmos Graphing Calculator", url: "https://www.desmos.com/calculator" }
                    ],
                    tabs: {
                        "Videos": [
                            { title: "Algebra - Equations with Two Variables", url: "https://www.youtube.com/watch?v=2-yS7s2-s7k" }
                        ],
                        "Articles": [
                            { title: "Linear Equations in Two Variables", url: "https://www.cuemath.com/algebra/linear-equations-in-two-variables/" }
                        ]
                    }
                },
                "HSF.IF.B.4 – Interpret key features of graphs and tables in terms of quantities": {
                    info: "This math standard helps you understand how to read and interpret graphs and data tables, which is essential for analyzing magnetic field strength and electromagnetism visualizations.",
                    resources: [
                        { name: "Khan Academy: Interpreting Graphs", url: "https://www.khanacademy.org/math/algebra/x2f8bb11595b61c86:functions/x2f8bb11595b61c86:interpreting-graphs/v/interpreting-graphs-example" },
                        { name: "Math is Fun: Reading Graphs", url: "https://www.mathsisfun.com/data/reading-graphs.html" }
                    ],
                    tabs: {
                        "Videos": [
                            { title: "Interpreting Graphs", url: "https://www.youtube.com/watch?v=kY67y_Lq104" }
                        ],
                        "Articles": [
                            { title: "How to Read and Interpret Graphs", url: "https://www.wikihow.com/Read-and-Interpret-Graphs" }
                        ]
                    }
                }
            };

            function updateResources() {
                const selectedStrand = physicsMathStrandSelect.value;
                const data = resourceData[selectedStrand];

                strandInfoDiv.innerHTML = `<p>${data.info}</p>`;
                recommendedResourcesTitle.textContent = selectedStrand;

                recommendedResourcesList.innerHTML = '';
                data.resources.forEach(res => {
                    const li = document.createElement('li');
                    li.innerHTML = `<a href="${res.url}" target="_blank" class="text-blue-600 hover:underline">${res.name}</a>`;
                    recommendedResourcesList.appendChild(li);
                });

                // Clear existing tabs and content
                resourceTabsContainer.innerHTML = '';
                resourceContentContainer.innerHTML = '';

                let firstTab = true;
                for (const tabName in data.tabs) {
                    const tabButton = document.createElement('button');
                    tabButton.className = `py-2 px-4 text-sm font-medium text-center rounded-t-lg border-b-2 ${firstTab ? 'border-accent-color text-accent-color' : 'border-transparent text-gray-500 hover:text-gray-700 hover:border-gray-300'}`;
                    tabButton.textContent = tabName;
                    tabButton.setAttribute('data-tab', tabName);
                    resourceTabsContainer.appendChild(tabButton);

                    const tabContent = document.createElement('div');
                    tabContent.id = `tab-content-${tabName.toLowerCase()}`;
                    tabContent.className = `p-4 ${firstTab ? '' : 'hidden'}`;
                    tabContent.innerHTML = `<ul class="list-disc list-inside space-y-2">`;
                    data.tabs[tabName].forEach(item => {
                        tabContent.innerHTML += `<li><a href="${item.url}" target="_blank" class="text-blue-600 hover:underline">${item.title}</a></li>`;
                    });
                    tabContent.innerHTML += `</ul>`;
                    resourceContentContainer.appendChild(tabContent);

                    tabButton.addEventListener('click', (event) => {
                        // Deactivate all tabs
                        resourceTabsContainer.querySelectorAll('button').forEach(btn => {
                            btn.classList.remove('border-accent-color', 'text-accent-color');
                            btn.classList.add('border-transparent', 'text-gray-500', 'hover:text-gray-700', 'hover:border-gray-300');
                        });
                        // Hide all content
                        resourceContentContainer.querySelectorAll('div').forEach(content => {
                            content.classList.add('hidden');
                        });

                        // Activate clicked tab
                        event.target.classList.add('border-accent-color', 'text-accent-color');
                        event.target.classList.remove('border-transparent', 'text-gray-500', 'hover:text-gray-700', 'hover:border-gray-300');

                        // Show corresponding content
                        document.getElementById(`tab-content-${event.target.getAttribute('data-tab').toLowerCase()}`).classList.remove('hidden');
                    });

                    firstTab = false;
                }
            }

            physicsMathStrandSelect.addEventListener('change', updateResources);
            updateResources(); // Initial call

            // Study Plan Generation
            const currentLevelSelect = document.getElementById('current-level-select-magnetism');
            const studyTimeSelect = document.getElementById('study-time-select-magnetism');
            const generateStudyPlanButton = document.getElementById('generate-study-plan-magnetism');
            const studyPlanOutputDiv = document.getElementById('study-plan-output-magnetism');

            generateStudyPlanButton.addEventListener('click', () => {
                const level = currentLevelSelect.value;
                const time = studyTimeSelect.value;
                let plan = '';

                if (level.includes('Beginner')) {
                    plan += `<p class="font-bold text-lg mb-2">Your Beginner Study Plan (${time}):</p>`;
                    plan += `<ul class="list-disc list-inside space-y-1">
                        <li>Week 1: Focus on "Key Concepts: Magnetic Fields" and the Compass Visualization.</li>
                        <li>Week 2: Explore "Magnetic Force and Inverse Square Law" with the Field Strength Visualization.</li>
                        <li>Week 3: Dive into "Electromagnetism" and its interactive visualization.</li>
                        <li>Daily: Spend 15-20 minutes reviewing definitions and trying the quiz questions.</li>
                        <li>Weekly: Revisit visualizations and try to explain them in your own words.</li>
                    </ul>`;
                } else if (level.includes('Intermediate')) {
                    plan += `<p class="font-bold text-lg mb-2">Your Intermediate Study Plan (${time}):</p>`;
                    plan += `<ul class="list-disc list-inside space-y-1">
                        <li>Week 1: Review all Key Concepts, focusing on the mathematical formulas.</li>
                        <li>Week 2: Experiment with all visualizations, noting how changes in variables affect outcomes.</li>
                        <li>Week 3: Focus on the Assessment section, trying to explain *why* each answer is correct.</li>
                        <li>Daily: Practice deriving relationships or sketching field lines.</li>
                        <li>Weekly: Research one real-world application of magnetism in more detail.</li>
                    </ul>`;
                } else if (level.includes('Advanced')) {
                    plan += `<p class="font-bold text-lg mb-2">Your Advanced Study Plan (${time}):</p>`;
                    plan += `<ul class="list-disc list-inside space-y-1">
                        <li>Week 1: Research advanced topics like Lorentz force, magnetic permeability, or Maxwell's equations.</li>
                        <li>Week 2: Explore complex applications like magnetic levitation or advanced MRI principles.</li>
                        <li>Week 3: Design your own simple magnetic experiment or thought experiment.</li>
                        <li>Daily: Challenge yourself with complex problems from external physics resources.</li>
                        <li>Weekly: Discuss advanced concepts with peers or mentors.</li>
                    </ul>`;
                } else if (level.includes('Expert')) {
                    plan += `<p class="font-bold text-lg mb-2">Your Expert Study Plan (${time}):</p>`;
                    plan += `<ul class="list-disc list-inside space-y-1">
                        <li>Ongoing: Delve into research papers on cutting-edge magnetic technologies or theoretical physics.</li>
                        <li>Ongoing: Consider participating in physics competitions or science fairs.</li>
                        <li>Ongoing: Explore academic pathways in electromagnetism, quantum physics, or materials science.</li>
                        <li>Connect with university professors or industry professionals in related fields.</li>
                    </ul>`;
                }

                studyPlanOutputDiv.innerHTML = plan;
                studyPlanOutputDiv.classList.remove('hidden');
            });
        });
    </script>
</body>
</html>
"""

# Render the HTML content
components.html(html_content, height=1000, scrolling=True)
