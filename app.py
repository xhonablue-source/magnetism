# app.py

import streamlit as st
import streamlit.components.v1 as components

# --- Page Setup ---
st.set_page_config(page_title="The Math of Magnetism", page_icon="🌌", layout="wide")

# --- Developer Credit (Matching the style of Panther Vision) ---
col1, col2 = st.columns([1, 4])
with col1:
    # Placeholder for Englewood STEM HS Logo - ensure you have 'englewood_stem_logo.png' in your project
    try:
        st.image("englewood_stem_logo.png", width=80)
    except:
        st.write("Logo Placeholder") # Fallback if logo file not found

with col2:
    st.markdown("### www.cognitivecloud.ai")
    st.markdown("**Developed for Englewood STEM HS by Xavier Honablue M.Ed**")

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
    <title>The Math of Magnetism: Unveiling Invisible Forces | Cognitive Cloud Education</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;700&display=swap" rel="stylesheet">
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
                The Math of Magnetism
            </a>
            <div class="hidden md:flex space-x-6 text-gray-700">
                <a href="#intro" class="nav-link">Intro</a>
                <a href="#concepts" class="nav-link">Concepts</a>
                <a href="#visualizations" class="nav-link">Visualizations</a>
                <a href="#quiz" class="nav-link">Quiz</a>
                <a href="#resources" class="nav-link">Resources</a>
                <a href="#study-plan" class="nav-link">Study Plan</a>
            </div>
            <button id="mobile-menu-button" class="md:hidden text-gray-700">
                <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16m-7 6h7"></path></svg>
            </button>
        </nav>
        <div id="mobile-menu" class="hidden md:hidden px-6 pb-4">
            <a href="#intro" class="block py-2 text-gray-700">Intro</a>
            <a href="#concepts" class="block py-2 text-gray-700">Concepts</a>
            <a href="#visualizations" class="block py-2 text-gray-700">Visualizations</a>
            <a href="#quiz" class="block py-2 text-gray-700">Quiz</a>
            <a href="#resources" class="block py-2 text-gray-700">Resources</a>
            <a href="#study-plan" class="block py-2 text-gray-700">Study Plan</a>
        </div>
    </header>

    <main class="container mx-auto px-6 py-8">
        <section id="intro" class="mb-12 p-6 bg-white rounded-lg shadow-md">
            <div class="flex items-center mb-4">
                <img src="https://placehold.co/80x80/005A9C/FFFFFF?text=ESH" alt="Englewood STEM HS Logo" class="w-20 h-20 mr-4 rounded-full">
                <div>
                    <h3 class="text-lg font-semibold accent-color">www.cognitivecloud.ai</h3>
                    <p class="text-sm text-gray-600">Developed for Englewood STEM HS by Xavier Honablue M.Ed</p>
                </div>
            </div>
            <hr class="my-6">
            <h1 class="text-4xl font-bold accent-color mb-4">🌌 The Math of Magnetism: Unveiling Invisible Forces</h1>
            <p class="text-lg text-gray-700 mb-4">
                Welcome, **Englewood STEM Panthers**! In this MathCraft lesson, **we** will explore how the invisible forces of magnetism are described and understood through the power of mathematics. From the compass guiding sailors to the MRI machines saving lives, magnetism is everywhere, and math is its language.
            </p>
            <hr class="my-6">
            <h3 class="text-2xl font-bold accent-color mb-3">🎯 Objective:</h3>
            <ul class="list-disc list-inside text-gray-700 space-y-2">
                <li>Understand the concept of magnetic fields and forces.</li>
                <li>Explore the inverse square law as it applies to magnetic strength.</li>
                <li>Discover the relationship between electricity and magnetism (electromagnetism).</li>
                <li>Connect abstract mathematical concepts to real-world magnetic phenomena.</li>
            </ul>
            <div class="bg-blue-100 border-l-4 border-blue-500 text-blue-700 p-4 mt-6 rounded-md" role="alert">
                <p class="font-bold">📚 Illinois Learning Standards Alignment:</p>
                <p>This lesson aligns with high school physics and mathematics standards, including understanding forces, inverse square relationships, and applying mathematical models to scientific phenomena.</p>
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
                <label for="learning-mode" class="block text-gray-700 text-lg font-medium mb-2">Pick your learning mode or style:</label>
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
            <p class="text-lg text-gray-700 mb-6">Before we dive into the visualizations, let's understand the core ideas that govern magnetism.</p>

            <div class="mb-8">
                <h3 class="text-2xl font-bold accent-color mb-3">Magnetic Fields</h3>
                <p class="text-gray-700 mb-4">
                    A magnetic field is an area around a magnet or a moving electric charge where magnetic force is exerted. We often visualize these fields using **magnetic field lines**, which show the direction a compass would point. The density of these lines indicates the strength of the field.
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
                    The force between two magnetic poles, or between a magnet and a magnetic material, follows an **inverse square law**. This means the magnetic force is inversely proportional to the square of the distance between them. As the distance increases, the force decreases rapidly.
                </p>
                <p class="text-gray-700 mb-4">
                    Mathematically, this can be expressed as: $F \propto 1/r^2$, where $F$ is the magnetic force and $r$ is the distance.
                </p>
            </div>

            <div>
                <h3 class="text-2xl font-bold accent-color mb-3">Electromagnetism</h3>
                <p class="text-gray-700 mb-4">
                    One of the most profound discoveries in physics is that electric currents create magnetic fields. This principle is called **electromagnetism**. The strength of an electromagnet depends on factors like the amount of current flowing through the wire and the number of coils in the wire.
                </p>
            </div>
        </section>

        <section id="visualizations" class="mb-12 p-6 bg-white rounded-lg shadow-md">
            <h2 class="text-3xl font-bold accent-color mb-4">📈 Interactive Magnetism Visualizations</h2>
            <p class="text-lg text-gray-700 mb-6">Let's see how changing variables affects magnetic phenomena.</p>

            <div class="mb-8">
                <h3 class="text-2xl font-bold accent-color mb-3">Magnetic Field Strength vs. Distance</h3>
                <p class="text-gray-700 mb-4">Observe how the magnetic field strength changes as the distance from a magnetic source increases. This demonstrates the inverse square law.</p>
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
                <p class="text-gray-700 mb-4">See how the strength of an electromagnet changes based on the current and the number of coils.</p>
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

        <section id="quiz" class="mb-12 p-6 bg-white rounded-lg shadow-md">
            <h2 class="text-3xl font-bold accent-color mb-4">🎲 Quick Understanding Check</h2>
            <div id="magnetism-quiz-questions">
                <!-- Quiz questions will be dynamically inserted here -->
            </div>
        </section>

        <section id="reflection" class="mb-12 p-6 bg-white rounded-lg shadow-md">
            <h2 class="text-3xl font-bold accent-color mb-4">🧾 Reflection</h2>
            <label for="reflection-text" class="block text-gray-700 text-lg font-medium mb-2">Describe one real-world application of magnetism that you find fascinating, and explain how mathematics helps us understand or utilize it.</label>
            <textarea id="reflection-text" rows="5" class="block w-full p-3 border border-gray-300 rounded-lg shadow-sm focus:ring-accent-color focus:border-accent-color"></textarea>
            <button id="submit-reflection" class="mt-4 bg-accent text-white font-bold py-3 px-6 rounded-lg hover:bg-opacity-90 transition-colors">Submit Reflection</button>
            <div id="reflection-feedback" class="mt-4 p-3 bg-green-100 text-green-700 rounded-md hidden"></div>
        </section>

        <section id="summary" class="mb-12 p-6 bg-white rounded-lg shadow-md">
            <h2 class="text-3xl font-bold accent-color mb-4">🎓 What You've Learned</h2>
            <p class="text-lg text-gray-700 mb-4">**Congratulations!** You've explored:</p>
            <ul class="list-disc list-inside text-gray-700 space-y-2">
                <li>✅ The fundamental concepts of **magnetic fields and forces**.</li>
                <li>✅ How the **inverse square law** describes magnetic strength.</li>
                <li>✅ The fascinating relationship of **electromagnetism**.</li>
                <li>✅ **Real-world applications** where the math of magnetism is crucial.</li>
            </ul>
            <p class="text-lg text-gray-700 mt-4">
                **Remember:** Magnetism is not just a mysterious force; it's a phenomenon that can be precisely described and manipulated using mathematical principles. By understanding these principles, **we** unlock the secrets of the universe and build the technologies of tomorrow!
            </p>
            <p class="text-xl font-bold text-accent-secondary mt-4">Keep your **Panther Vision** sharp and explore the invisible forces all around you! 🐾</p>
        </section>

        <section id="resources" class="mb-12 p-6 bg-white rounded-lg shadow-md">
            <h2 class="text-3xl font-bold accent-color mb-4">📚 Further Exploration & Resources</h2>
            <h3 class="text-2xl font-bold accent-color mb-3">🎯 Choose Your Learning Focus</h3>
            <label for="physics-math-strand" class="block text-gray-700 text-lg font-medium mb-2">Select a Physics/Math Strand to customize your resources:</label>
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
                                title: { display: true, text: 'Strength (arbitrary units)' }
                            }
                        },
                        plugins: {
                            legend: { display: false },
                            tooltip: {
                                callbacks: {
                                    label: function(context) {
                                        return `Distance: ${context.parsed.x.toFixed(1)}, Strength: ${context.parsed.y.toFixed(2)}`;
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
                return current * coils; // Simplified model
            }

            function updateElectromagnetChart() {
                const current = parseFloat(currentSlider.value);
                const coils = parseInt(coilsSlider.value);

                currentValueSpan.textContent = current.toFixed(1);
                coilsValueSpan.textContent = coils;

                const strength = calculateElectromagnetStrength(current, coils);
                electromagnetStrengthValueSpan.textContent = strength.toFixed(2);

                if (electromagnetChart) {
                    electromagnetChart.destroy();
                }

                electromagnetChart = new Chart(electromagnetChartCtx, {
                    type: 'bar',
                    data: {
                        labels: ['Current (Amps)', 'Coils', 'Calculated Strength'],
                        datasets: [{
                            label: 'Value',
                            data: [current, coils, strength],
                            backgroundColor: ['#005A9C', '#F2A900', '#3b82f6'], // Blue, Orange, Lighter Blue
                            borderColor: ['#004B80', '#D99500', '#2563eb'],
                            borderWidth: 1
                        }]
                    },
                    options: {
                        responsive: true,
                        maintainAspectRatio: false,
                        scales: {
                            y: {
                                beginAtZero: true,
                                max: Math.max(currentSlider.max, coilsSlider.max, strength) * 1.1 // Adjust max for better visualization
                            }
                        },
                        plugins: {
                            legend: { display: false },
                            tooltip: {
                                callbacks: {
                                    label: function(context) {
                                        return `${context.label}: ${context.parsed.y.toFixed(2)}`;
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

            // Quick Understanding Check (Magnetism Specific)
            const magnetismQuizQuestions = [
                {
                    question: "What happens to the magnetic force as the distance between magnets increases?",
                    options: ["It increases", "It decreases rapidly", "It stays the same", "It becomes infinite"],
                    correct: "It decreases rapidly",
                    explanation: "Magnetic force follows an inverse square law, meaning it decreases quickly with distance."
                },
                {
                    question: "Which of these factors increases the strength of an electromagnet?",
                    options: ["Decreasing the current", "Decreasing the number of coils", "Increasing the current", "Using a non-magnetic core"],
                    correct: "Increasing the current",
                    explanation: "Both increasing current and number of coils strengthen an electromagnet."
                },
                {
                    question: "Magnetic field lines typically emerge from which pole of a magnet?",
                    options: ["South pole", "North pole", "Center", "They don't emerge from poles"],
                    correct: "North pole",
                    explanation: "By convention, magnetic field lines emerge from the North pole and enter the South pole."
                }
            ];

            const magnetismQuizContainer = document.getElementById('magnetism-quiz-questions');
            magnetismQuizQuestions.forEach((q, qIndex) => {
                const questionDiv = document.createElement('div');
                questionDiv.classList.add('mb-6', 'p-4', 'bg-gray-50', 'rounded-lg', 'shadow-sm');
                questionDiv.innerHTML = `
                    <p class="font-bold text-gray-800 mb-3">${q.question}</p>
                    <div id="magnetism-options-${qIndex}" class="space-y-2"></div>
                    <button class="check-magnetism-answer mt-4 bg-accent text-white font-bold py-2 px-4 rounded-lg hover:bg-opacity-90 transition-colors" data-index="${qIndex}">Check Answer</button>
                    <div id="magnetism-feedback-${qIndex}" class="mt-3 text-sm hidden"></div>
                `;
                const optionsDiv = questionDiv.querySelector(`#magnetism-options-${qIndex}`);
                q.options.forEach((option, oIndex) => {
                    const radioDiv = document.createElement('div');
                    radioDiv.innerHTML = `
                        <input type="radio" id="magnetism-quiz-${qIndex}-option-${oIndex}" name="magnetism-quiz-q-${qIndex}" value="${option}" class="mr-2 accent-color">
                        <label for="magnetism-quiz-${qIndex}-option-${oIndex}" class="text-gray-700">${option}</label>
                    `;
                    optionsDiv.appendChild(radioDiv);
                });
                magnetismQuizContainer.appendChild(questionDiv);
            });

            magnetismQuizContainer.querySelectorAll('.check-magnetism-answer').forEach(button => {
                button.addEventListener('click', (event) => {
                    const index = event.target.dataset.index;
                    const selectedOption = document.querySelector(`input[name="magnetism-quiz-q-${index}"]:checked`);
                    const feedbackDiv = document.getElementById(`magnetism-feedback-${index}`);
                    feedbackDiv.classList.remove('hidden', 'bg-green-100', 'text-green-700', 'bg-red-100', 'text-red-700');

                    if (selectedOption && selectedOption.value === magnetismQuizQuestions[index].correct) {
                        feedbackDiv.textContent = `✅ Correct! ${magnetismQuizQuestions[index].explanation}`;
                        feedbackDiv.classList.add('bg-green-100', 'text-green-700');
                    } else {
                        feedbackDiv.textContent = `❌ Try again! The correct answer is ${magnetismQuizQuestions[index].correct}. ${magnetismQuizQuestions[index].explanation}`;
                        feedbackDiv.classList.add('bg-red-100', 'text-red-700');
                    }
                });
            });

            // Reflection
            const reflectionTextarea = document.getElementById('reflection-text');
            const submitReflectionButton = document.getElementById('submit-reflection');
            const reflectionFeedbackDiv = document.getElementById('reflection-feedback');

            submitReflectionButton.addEventListener('click', () => {
                if (reflectionTextarea.value.trim()) {
                    reflectionFeedbackDiv.textContent = "✅ Excellent scientific thinking! You're connecting math to the real world!";
                    reflectionFeedbackDiv.classList.remove('hidden', 'bg-red-100', 'text-red-700');
                    reflectionFeedbackDiv.classList.add('bg-green-100', 'text-green-700');
                } else {
                    reflectionFeedbackDiv.textContent = "Please share your thoughts to complete the reflection.";
                    reflectionFeedbackDiv.classList.remove('hidden', 'bg-green-100', 'text-green-700');
                    reflectionFeedbackDiv.classList.add('bg-red-100', 'text-red-700');
                }
            });

            // Resources Section
            const physicsMathStrandSelect = document.getElementById('physics-math-strand');
            const strandInfoMagnetismDiv = document.getElementById('strand-info-magnetism');
            const recommendedResourcesTitle = document.getElementById('recommended-resources-title');
            const recommendedResourcesList = document.getElementById('recommended-resources-list');
            const magnetismResourceTabsContainer = document.querySelector('#magnetism-resource-tabs-container nav');
            const magnetismResourceContentContainer = document.getElementById('magnetism-resource-content-container');

            const magnetismResources = {
                "📺 Video Tutorials": [
                    { name: "Khan Academy - Magnetism", url: "https://www.khanacademy.org/science/physics/magnetic-forces-and-magnetic-fields", description: "Comprehensive video series on magnetic forces and fields." },
                    { name: "Physics Classroom - Magnetism", url: "https://www.physicsclassroom.com/class/circuits/Lesson-4/Magnetism", description: "Tutorials on magnetic concepts and principles." },
                    { name: "Veritasium - Magnets: How Do They Work?", url: "https://www.youtube.com/watch?v=hFAOXzXrX2I", description: "Engaging video explaining the fundamental nature of magnets." }
                ],
                "💻 Interactive Tools": [
                    { name: "PhET Electromagnetism Simulation", url: "https://phet.colorado.edu/sims/html/faraday/latest/faraday_en.html", description: "Interactive simulation to explore electromagnets and Faraday's Law." },
                    { name: "GeoGebra Magnetic Field Visualizer", url: "https://www.geogebra.org/m/k2984k83", description: "Visualize magnetic fields from various sources." }
                ],
                "📚 Study Guides & Practice": [
                    { name: "HyperPhysics - Magnetism", url: "http://hyperphysics.phy-astr.gsu.edu/hbase/magnetic/magcon.html", description: "Detailed concepts and equations related to magnetism." },
                    { name: "SparkNotes - Magnetism", url: "https://www.sparknotes.com/physics/magnetism/", description: "Study guide with summaries and quizzes on magnetism." }
                ],
                "📖 Reference Materials": [
                    { name: "NGSS - Forces and Interactions", url: "https://www.nextgenscience.org/topic-arrangement/hsps2-forces-and-interactions", description: "Next Generation Science Standards for high school physics." },
                    { name: "Wikipedia - Magnetism", url: "https://en.wikipedia.org/wiki/Magnetism", description: "Comprehensive overview of magnetism." }
                ]
            };

            const recommendedMagnetismResources = {
                "HS-PS2-5 – Forces and Motion: Electric and Magnetic Fields": [
                    "Khan Academy - Magnetic Forces and Fields",
                    "PhET Electromagnetism Simulation",
                    "HyperPhysics - Magnetism"
                ],
                "HS-PS3-2 – Energy: Electromagnetism and Energy Conversion": [
                    "PhET Electromagnetism Simulation",
                    "Veritasium - Magnets: How Do They Work?",
                    "Physics Classroom - Magnetism"
                ],
                "HSA.CED.A.2 – Create equations in two or more variables to represent relationships between quantities": [
                    "HyperPhysics - Magnetism (focus on equations)",
                    "Khan Academy - Magnetic Force on a Current-Carrying Wire"
                ],
                "HSF.IF.B.4 – Interpret key features of graphs and tables in terms of quantities": [
                    "Magnetic Field Strength vs. Distance (this app's visualization)",
                    "Physics Classroom - Magnetism (graph interpretation)"
                ]
            };

            function updateRecommendedResources() {
                const selectedStrand = physicsMathStrandSelect.value;
                let emphasisText = "";
                let priorityResources = [];

                if (selectedStrand.includes("HS-PS2-5")) {
                    emphasisText = "Focus: Electric and Magnetic Fields";
                    priorityResources = recommendedMagnetismResources["HS-PS2-5 – Forces and Motion: Electric and Magnetic Fields"];
                } else if (selectedStrand.includes("HS-PS3-2")) {
                    emphasisText = "Focus: Electromagnetism and Energy Conversion";
                    priorityResources = recommendedMagnetismResources["HS-PS3-2 – Energy: Electromagnetism and Energy Conversion"];
                } else if (selectedStrand.includes("HSA.CED.A.2")) {
                    emphasisText = "Focus: Creating Equations for Relationships";
                    priorityResources = recommendedMagnetismResources["HSA.CED.A.2 – Create equations in two or more variables to represent relationships between quantities"];
                } else if (selectedStrand.includes("HSF.IF.B.4")) {
                    emphasisText = "Focus: Interpreting Graphs and Quantities";
                    priorityResources = recommendedMagnetismResources["HSF.IF.B.4 – Interpret key features of graphs and tables in terms of quantities"];
                }

                strandInfoMagnetismDiv.textContent = `🎯 ${emphasisText}`;
                strandInfoMagnetismDiv.classList.remove('hidden');

                recommendedResourcesList.innerHTML = '';
                priorityResources.forEach(resourceName => {
                    const listItem = document.createElement('li');
                    listItem.classList.add('flex', 'items-start');
                    listItem.innerHTML = `⭐ <span class="ml-2 font-bold">${resourceName}</span>`;
                    recommendedResourcesList.appendChild(listItem);
                });
            }
            physicsMathStrandSelect.addEventListener('change', updateRecommendedResources);
            updateRecommendedResources(); // Initial call

            // Populate Additional Learning Resources tabs
            let currentResourceTab = null;
            Object.keys(magnetismResources).forEach((category, index) => {
                const button = document.createElement('button');
                button.classList.add('resource-tab', 'whitespace-nowrap', 'py-4', 'px-1', 'border-b-2', 'border-transparent', 'text-gray-500', 'hover:text-gray-700', 'hover:border-gray-300', 'font-medium', 'text-sm');
                button.textContent = category;
                button.dataset.category = category;
                magnetismResourceTabsContainer.appendChild(button);

                const contentDiv = document.createElement('div');
                contentDiv.classList.add('resource-tab-pane', 'hidden', 'p-4', 'bg-gray-50', 'rounded-lg', 'shadow-sm');
                contentDiv.id = `resource-pane-${index}`;
                magnetismResources[category].forEach(item => {
                    contentDiv.innerHTML += `
                        <p class="font-bold text-gray-800 mb-1"><a href="${item.url}" target="_blank" class="text-accent-color hover:underline">${item.name}</a></p>
                        <p class="text-gray-700 mb-3">📝 ${item.description}</p>
                        <hr class="my-2 border-gray-200">
                    `;
                });
                magnetismResourceContentContainer.appendChild(contentDiv);
            });

            function activateResourceTab(category) {
                document.querySelectorAll('.resource-tab').forEach(btn => {
                    if (btn.dataset.category === category) {
                        btn.classList.add('active', 'border-accent-color', 'text-accent-color');
                        btn.classList.remove('border-transparent', 'text-gray-500', 'hover:text-gray-700', 'hover:border-gray-300');
                    } else {
                        btn.classList.remove('active', 'border-accent-color', 'text-accent-color');
                        btn.classList.add('border-transparent', 'text-gray-500', 'hover:text-gray-700', 'hover:border-gray-300');
                    }
                });
                document.querySelectorAll('.resource-tab-pane').forEach(pane => {
                    if (pane.id === `resource-pane-${Object.keys(magnetismResources).indexOf(category)}`) {
                        pane.classList.remove('hidden');
                    } else {
                        pane.classList.add('hidden');
                    }
                });
            }

            magnetismResourceTabsContainer.querySelectorAll('.resource-tab').forEach(button => {
                button.addEventListener('click', (event) => {
                    activateResourceTab(event.target.dataset.category);
                });
            });
            activateResourceTab(Object.keys(magnetismResources)[0]); // Activate first tab by default

            // Study Plan Generator
            const currentLevelSelectMagnetism = document.getElementById('current-level-select-magnetism');
            const studyTimeSelectMagnetism = document.getElementById('study-time-select-magnetism');
            const generateStudyPlanButtonMagnetism = document.getElementById('generate-study-plan-magnetism');
            const studyPlanOutputMagnetismDiv = document.getElementById('study-plan-output-magnetism');

            generateStudyPlanButtonMagnetism.addEventListener('click', () => {
                const currentLevel = currentLevelSelectMagnetism.value;
                const studyTime = studyTimeSelectMagnetism.value;
                let planContent = "";
                let tip = "";

                if (currentLevel.includes("Beginner")) {
                    planContent = `
                        <h3 class="text-xl font-bold accent-color mb-2">Week 1-2: Foundations of Magnetism</h3>
                        <ul class="list-disc list-inside text-gray-700 space-y-1">
                            <li>Watch Khan Academy's "Magnetism" intro videos.</li>
                            <li>Explore the PhET Electromagnetism Simulation to get a feel for fields.</li>
                            <li>Complete the Quick Understanding Check quizzes in this app.</li>
                        </ul>
                        <h3 class="text-xl font-bold accent-color mt-4 mb-2">Week 3-4: Magnetic Force & Fields</h3>
                        <ul class="list-disc list-inside text-gray-700 space-y-1">
                            <li>Focus on understanding magnetic field lines and poles.</li>
                            <li>Experiment with the "Magnetic Field Strength vs. Distance" visualization.</li>
                            <li>Read the Physics Classroom tutorials on magnetism.</li>
                        </ul>
                    `;
                } else if (currentLevel.includes("Intermediate")) {
                    planContent = `
                        <h3 class="text-xl font-bold accent-color mb-2">Week 1: Reinforce Basics & Electromagnetism</h3>
                        <ul class="list-disc list-inside text-gray-700 space-y-1">
                            <li>Review basic magnetic concepts.</li>
                            <li>Deep dive into the "Electromagnet Strength" visualization, changing current and coils.</li>
                            <li>Read about the Right-Hand Rule for current and magnetic fields.</li>
                        </ul>
                        <h3 class="text-xl font-bold accent-color mt-4 mb-2">Week 2-3: Applications & Problem Solving</h3>
                        <ul class="list-disc list-inside text-gray-700 space-y-1">
                            <li>Research real-world applications like electric motors and generators.</li>
                            <li>Try to explain how a compass works using magnetic field concepts.</li>
                            <li>Work through practice problems on magnetic force calculations (from online resources).</li>
                        </ul>
                    `;
                } else if (currentLevel.includes("Advanced")) {
                    planContent = `
                        <h3 class="text-xl font-bold accent-color mb-2">Week 1: Advanced Electromagnetic Concepts</h3>
                        <ul class="list-disc list-inside text-gray-700 space-y-1">
                            <li>Explore Faraday's Law of Induction and Lenz's Law.</li>
                            <li>Research magnetic materials (ferromagnetism, paramagnetism, diamagnetism).</li>
                            <li>Investigate the math behind magnetic flux.</li>
                        </ul>
                        <h3 class="text-xl font-bold accent-color mt-4 mb-2">Week 2: Future Technologies & Research</h3>
                        <ul class="list-disc list-inside text-gray-700 space-y-1">
                            <li>Research technologies like MRI, maglev trains, or fusion reactors.</li>
                            <li>Consider how quantum mechanics relates to magnetism.</li>
                            <li>Propose a new application of electromagnetism.</li>
                        </ul>
                    `;
                } else { // Expert
                    planContent = `
                        <h3 class="text-xl font-bold accent-color mb-2">Ongoing Challenge Plan:</h3>
                        <ul class="list-disc list-inside text-gray-700 space-y-1">
                            <li>Dive into vector calculus for advanced electromagnetism (Maxwell's Equations).</li>
                            <li>Mentor other students in magnetism and physics.</li>
                            <li>Explore current research in condensed matter physics or plasma physics related to magnetism.</li>
                        </ul>
                    `;
                }

                if (studyTime.includes("1-2 hours")) {
                    tip = "💡 **Tip:** Focus on mastering one concept per session. Short, consistent practice is key!";
                } else if (studyTime.includes("3-4 hours")) {
                    tip = "💡 **Tip:** Balance conceptual understanding with problem-solving practice. Use interactive tools to visualize.";
                } else if (studyTime.includes("5-6 hours")) {
                    tip = "💡 **Tip:** Challenge yourself with more complex problems and try to explain concepts to a peer.";
                } else { // 7+ hours
                    tip = "💡 **Tip:** Consider exploring university-level physics resources or engaging in science fair projects related to magnetism.";
                }

                studyPlanOutputMagnetismDiv.innerHTML = `<p class="font-bold text-green-700 mb-3">🎯 Your Personalized Magnetism Mastery Plan:</p>${planContent}<p class="mt-4 text-blue-700">${tip}</p>`;
                studyPlanOutputMagnetismDiv.classList.remove('hidden');
                studyPlanOutputMagnetismDiv.classList.add('bg-green-50', 'border-l-4', 'border-green-500');
            });

            // Initial calls
            updateWelcomeMessage();
            // Removed previous function calls that were causing errors.
        });
    </script>
</body>
</html>
"""

# Render the HTML in Streamlit
st.components.v1.html(html_content, height=2000, scrolling=True)

# requirements.txt for Streamlit
st.markdown("---")
st.subheader("`requirements.txt` for this Streamlit application:")
st.code("""
streamlit
""", language="text")
