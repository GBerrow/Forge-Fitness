# Forge Fitness

**A comprehensive fitness guidance platform designed to empower users in structuring and managing their personal fitness journeys.**

![Forge Fitness Banner](assets/images/readme-images/Forge-fitness-intro-image.png)

## Introduction

Forge Fitness is a modern, full-stack Django web application that serves as an **educational and organizational tool** for fitness enthusiasts of all levels. Unlike traditional fitness tracking applications that focus on real-time data collection, Forge Fitness takes a unique approach by **teaching users how to effectively manage their fitness journey** through structured guidance, goal-setting frameworks, and progress visualization techniques.

Built with a **demonstration-first philosophy**, the platform empowers users to understand the fundamental principles of successful fitness management rather than simply recording workout data. Through carefully designed user interfaces and educational workflows, users learn to create sustainable fitness routines, set meaningful milestones, and develop the organizational skills necessary for long-term success.

The application addresses a critical gap in the fitness app market: **the need for structured learning and habit formation**. While most fitness apps overwhelm users with complex tracking features, Forge Fitness focuses on **building foundational knowledge** through intuitive dashboards, guided workout planning, and progressive achievement systems. This approach has been informed by extensive market research showing that **72% of fitness app users prefer personalized guidance** and that **structured goal-setting increases user retention by 75%**.

By combining modern web development practices with proven fitness psychology principles, Forge Fitness creates an environment where users can **practice and internalize effective fitness management strategies** before applying them to their real-world routines. The result is a platform that doesn't just track progress—it teaches users how to create, maintain, and optimize their own fitness success systems.

---

### Before Continuing Further:

**Fancy having a look at my testing documentation?** [👉 Click Here!](./testing/test.md)

**Head on over to the deployed site** [👉 Click Here!](https://forge-fitness-d9cu.onrender.com/signup/)

## What Makes Forge Fitness Different?

🎯 **Education-First Approach**: Rather than simply tracking workouts, Forge Fitness teaches users the **fundamental principles of effective fitness management**. The platform guides users through proven methodologies for goal setting, progress monitoring, and habit formation. Each section includes educational content that helps users understand **why** certain practices work, not just **how** to implement them, creating lasting fitness knowledge that extends beyond the app.

![Education Dashboard](assets/images/readme-images/education-dashboard.png)

🏗️ **Structured Guidance**: Provides comprehensive frameworks for workout planning, activity logging, and milestone tracking that users can apply to their personal fitness routines. The platform breaks down complex fitness concepts into **digestible, actionable steps** with clear progression paths. Users learn to structure their training across different muscle groups, understand periodization principles, and develop sustainable routines that fit their lifestyle and fitness level.

![Structured Guidance](assets/images/readme-images/structured-guidance.png)

📊 **Progress Visualization**: Demonstrates how to effectively monitor fitness progress through intuitive dashboards and achievement systems. The platform showcases **multiple methods of tracking success** beyond just numbers—from consistency streaks and personal records to goal completion rates and performance trends. Users discover how to identify patterns in their fitness journey and make data-driven adjustments to optimize their results.

![Progress Visualization](assets/images/readme-images/progress-note.png)

🔧 **Personalization Tools**: Offers customizable profiles, training plans, and settings that adapt to individual fitness goals and preferences. The platform teaches users how to **tailor their fitness approach** to their unique circumstances, whether they're focused on weight loss, muscle gain, endurance building, or general health improvement. From customizable workout templates to personalized milestone tracking, every feature can be adapted to match individual needs and preferences.

![Custom Profile](assets/images/readme-images/custom-profile.png)

💡 **Holistic Fitness Management**: Goes beyond individual workouts to address the **complete fitness ecosystem**—teaching users how to balance training, recovery, goal setting, and lifestyle factors. The platform demonstrates how to create sustainable fitness habits that integrate seamlessly with daily life, ensuring long-term success rather than short-term gains.

## Key Features at a Glance

- **🔐 User Authentication & Profiles**: Secure account management with comprehensive profile customization, including bio creation, profile picture uploads, and personalized fitness goal setting to create a tailored experience for each user's unique journey.

- **🏋️ Training Plan Builder**: Expertly structured workout guidance spanning all major muscle groups (chest, back, legs, shoulders, arms, core) with progressive training plans designed for beginners through advanced athletes, complete with exercise demonstrations and technique insights.

- **📊 Activity Logging System**: Comprehensive tracking ecosystem for daily movement, structured workouts, and fitness achievements, featuring milestone recognition, streak tracking, and personal record celebrations to maintain long-term motivation and accountability.

- **📈 Dashboard & Analytics**: Intuitive visual progress tracking with real-time performance insights, goal completion percentages, and trend analysis that transforms raw fitness data into actionable intelligence for continuous improvement.

- **⚙️ Settings & Customization**: Complete account control with granular preference management, secure data handling, and flexible customization options that ensure your fitness platform adapts to your evolving needs and privacy requirements.

Whether you're a **fitness newcomer** seeking structured, step-by-step guidance to confidently begin your wellness journey, or a **seasoned athlete** looking to systematically organize, analyze, and optimize your training methodology, Forge Fitness bridges the gap between fitness theory and practical application. Through its clean, intuitive interface and comprehensive educational approach, the platform empowers users to not just track their fitness—but to truly understand and master the art of sustainable, goal-oriented training that delivers lasting results.

---

**Sign up to gain full access of the live application** [👉 Click Here](https://forge-fitness-d9cu.onrender.com/signup/)

**If you want to check the testing documentation** [👉 Click Here]

---

## Table of Contents

This comprehensive documentation provides a complete overview of the Forge Fitness project, from initial concept and user experience design through to technical implementation and deployment. Whether you're interested in understanding the user-centered design approach, exploring the technical architecture, or setting up the application locally, each section contains detailed information to support developers, stakeholders, and users alike. The documentation follows industry best practices and includes visual examples, code snippets, and step-by-step instructions to ensure clarity and accessibility.

- [Introduction](#introduction)
- [Table of Contents](#table-of-contents)
- [Target Audience & User Needs](#target-audience--user-needs)
  - [Beginners & First-Time Gym-Goers](#beginners--first-time-gym-goers)
  - [Intermediate Users & Returning Lifters](#intermediate-users--returning-lifters)
  - [Advanced Gym-Goers](#advanced-gym-goers)
  - [Digital-First & Time-Conscious Users](#digital-first--time-conscious-users)
  - [Progress-Focused & Analytical Users](#progress-focused--analytical-users)
- [Client Goals](#client-goals)
- [User Stories](#user-stories)
- [Statistics](#statistics)
- [Initial Design](#initial-design)
  - [Colour Scheme](#colour-scheme)
  - [Typography](#typography)
- [Wireframes](#wireframes)
   - [Sign up Page](#sign-up-page)
   - [Login Page](#login-page)
   - [Home Page](#home-page)
   - [Workout Page](#workout-page)
   - [Progress Page](#progress-page)
   - [Profile Page](#profile-page)
   - [Settings Page](#settings-page)
- [User Experience | Final Design](#user-experience--final-design)
  - [Dashboard Overview](#dashboard-overview)
  - [Sign Up Page | Final Design](#sign-up-page--final-design)
  - [Login Page | Final Design](#login-page--final-design)
  - [Training Page | Final Design](#training-page--final-design)
  - [Activity Page | Final Design](#activity-page--final-design)
  - [Progression Page | Final Design](#progression-page--final-design)
  - [Settings Page | Final Design](#settings-page--final-design)
  - [Final Thoughts](#final-thoughts)
- [Database Structure](#database-structure)
- [Folder Structure](#folder-structure)
- [Technologies Used](#technologies-used)
- [Security Features](#security-features)
- [Testing](#testing)
- [Future Enhancements](#future-enhancements)
- [Local Development Setup](#local-development-setup)
- [Deployment](#deployment)
- [Credits](#credits)

---

## Target Audience & User Needs

Forge Fitness is designed as a structured, educational platform that empowers users at all levels of fitness by combining intuitive workout planning, progress tracking, and clear instructional guidance. Its core mission is to make fitness feel achievable, understandable, and trackable — whether you're stepping into the gym for the first time or optimizing a long-term program.

### Beginners & First-Time Gym-Goers

- **Step-by-Step Guidance**: Introductory workout plans, simplified UI, and clear instructions help users build confidence from day one.
- **Educational Focus**: Clear explanations of exercises, muscle groups, and routines foster learning, not just repetition.
- **Friendly Visuals**: Simple dashboards visualize improvement and reinforce early wins to encourage consistency.
- **Low Pressure**: No forced public sharing or performance comparison — the focus is on learning and personal growth.

### Intermediate Users & Returning Lifters

- **Structured Progression Tools**: Users can build and modify their training plans with progressive overload principles in mind.
- **Performance Logging**: Integrated activity logs help users see patterns, plateaus, and progress over time.
- **Training Phase Awareness**: Learn how to alternate between hypertrophy, strength, and recovery through visual breakdowns and plan suggestions.
- **Accountability Mechanisms**: Habit tracking and milestone visuals reinforce long-term routine building.

### Advanced Gym-Goers

- **Precision Tools**: Plan detailed training splits, log PRs, and monitor weekly or monthly progress with charts and analytics.
- **Customization**: Adjust plan templates or create routines from scratch using the training plan builder.
- **Data Insight**: Access personal performance summaries via bar, pie, and line graphs to aid decision-making.
- **Streamlined Interface**: A clutter-free dashboard allows fast access to training history and upcoming sessions.

### Digital-First & Time-Conscious Users

- **Fully Responsive Web App**: Works on mobile, tablet, and desktop without requiring downloads or installation.
- **Instant Access to Tools**: Users can build a plan, track a session, or review data in just a few clicks.
- **Clean Design**: Prioritizes accessibility, with a consistent layout and intuitive navigation.
- **Privacy by Design**: Users retain full control over their data, with secure login and account options.

### Progress-Focused & Analytical Users

- **Visual Performance Tracking**: Real-time updates to charts and dashboards based on logged activities.
- **Milestone System**: Log and visualize achievements such as workout streaks, strength milestones, or completed plans.
- **Insightful Patterns**: Identify training gaps, plateaus, or areas of strength with easy-to-interpret visuals.
- **Goal Alignment**: Set personal goals and ensure workouts contribute toward them with tracking and reminders.

Forge Fitness does more than just log workouts — it guides users through educational progression, empowering them to understand, structure, and sustain their training. Each feature is carefully mapped to the real needs of users at different stages in their fitness journey. For a deeper dive into these tools and how they're implemented, see the [Features](#features) section.

The diverse target audience directly supports the **core client objectives** of Forge Fitness. By serving beginners through advanced users, the platform demonstrates **user-friendly navigation** that scales with expertise levels, **comprehensive personalization** that adapts to individual fitness journeys, and **structured guidance** that educates while motivating. This multi-tiered approach ensures that whether users seek simple workout logging or complex training analytics, Forge Fitness delivers an **intuitive, secure, and engaging experience** that grows with their fitness development — ultimately creating a sustainable platform that retains users long-term while meeting diverse fitness management needs.

---

## Client Goals

The Forge Fitness application combines modern development practices with proven design patterns from industry leaders like PureGym, Garmin, and Strava. This milestone project showcases full-stack development capabilities while delivering a comprehensive fitness platform. By implementing features found in successful fitness applications and adding innovative elements, Forge Fitness demonstrates both technical proficiency and user-centered design principles. The following core objectives guide the development process and feature implementation:

### **1. User-Friendly and Intuitive Navigation**
**Objective**: Create a seamless, accessible experience that reduces friction and encourages consistent usage.

- The **Dashboard** serves as a central hub, allowing users to quickly access key sections such as **Profile, Training, Activity, Progress, and Settings**.
- Each section is designed with a minimalistic layout, making navigation effortless while ensuring all features remain accessible.
- Responsive UI elements ensure an optimal experience across different devices, supporting the 92% of fitness app users who access platforms via mobile.
- **Clear visual hierarchy** and **consistent design patterns** reduce cognitive load and support users of all technical skill levels.

**Business Impact**: Intuitive navigation directly correlates with user retention, as 25% of fitness app users abandon applications after poor initial experiences.

### **2. Personalization and User Control**
**Objective**: Empower users to customize their experience while maintaining full control over their data and preferences.

- The **Profile Page** allows users to personalize their experience by setting their **preferred name and bio**, as well as uploading a profile picture.
- The **Settings Page** includes essential options such as **Feedback, Support, and Account Deletion**, ensuring users can manage their preferences effectively.
- Users can track their fitness progress in the **Progression Page**, which focuses on **Goal Setting, Performance Tracking, and Personalized Feedback**.
- **Flexible customization options** adapt to individual fitness goals, whether focused on weight loss, muscle gain, or endurance improvement.

**Business Impact**: 72% of users prefer apps that allow personalized fitness plans, and personalized experiences increase goal completion rates by 50%.

### **3. Structured Training Guidance**
**Objective**: Provide educational, progressive fitness guidance that builds user confidence and knowledge.

- The **Training Section** provides users with a well-organized framework for fitness improvement:
  - **Introduction:** Guides users on how to use the training section effectively
  - **Workouts:** Covers different muscle groups and recommended exercises with proper form guidance
  - **Training Plans:** Helps users structure their fitness routine with progressive overload principles
  - **Summary:** Highlights key takeaways to keep users engaged and informed
- **Educational approach** teaches users the "why" behind fitness practices, not just the "how"
- **Scalable content** serves beginners through advanced users with appropriate complexity levels

**Business Impact**: Structured guidance increases user confidence and long-term adherence, addressing the common problem of gym intimidation among beginners.

### **4. Motivation through Progress Tracking**
**Objective**: Maintain user engagement through meaningful progress visualization and achievement recognition.

- The **Activity Page** enables users to monitor their daily activity, ensuring they stay consistent with their fitness goals:
  - **Daily Activity:** Summarizes movement trends and patterns
  - **Workout Tracking:** Encourages users to log and analyze their workouts
  - **Achievements:** Recognizes and celebrates fitness milestones and streaks
- **Visual progress indicators** provide immediate feedback and motivation
- **Milestone system** creates psychological rewards that encourage continued engagement

**Business Impact**: Users who actively track progress show 68% retention rates at 12 months versus 32% for non-tracking users.

### **5. Secure and Accessible Authentication**
**Objective**: Provide robust security while maintaining ease of access and user trust.

- The **Login Page** provides a secure authentication system with multiple login options (username or email)
- The **Sign-Up Page** ensures a smooth onboarding process with clear input fields and guided registration
- **Custom authentication backend** supports flexible login methods while maintaining security standards
- **Data protection measures** ensure user information remains private and secure
- **Account management tools** give users full control over their data and account status

**Business Impact**: Secure, user-friendly authentication reduces signup friction while building trust, essential for long-term user retention.

### **6. Feedback and Continuous Engagement**
**Objective**: Create feedback loops that drive continuous improvement and sustained user engagement.

- The **Settings Page** integrates feedback and support options, enabling users to report issues, request assistance, and suggest improvements
- The platform encourages ongoing engagement through motivational elements like **progress tracking and achievements**
- **User-driven insights** help identify areas for platform improvement and feature development
- **Community support mechanisms** create pathways for user assistance and engagement

**Business Impact**: Platforms with integrated feedback systems see 40% higher user satisfaction and 25% increased interaction rates.

### Strategic Alignment

The **Forge Fitness** application balances functionality and simplicity, ensuring that users can efficiently **track their workouts, manage their profile, stay motivated, and personalize their experience**. Each client goal directly addresses documented user needs and market research findings, creating a platform that not only meets technical requirements but delivers genuine value to fitness enthusiasts at every level.

These strategic objectives translate directly into specific user stories and feature implementations, ensuring that every development decision serves both user needs and business goals. The following user stories demonstrate how these high-level objectives manifest in practical, user-centered functionality that drives engagement and supports long-term fitness success.

---

## User Stories

The following user stories guided the development of Forge Fitness, ensuring every feature aligns with documented user needs and serves the platform's educational and motivational focus. Stories are organized by functional areas—each mapped to clearly defined user types: **Beginners**, **Intermediate/Advanced Users**, **Progress-Focused Users**, and **Mobile-First Users**.

These stories are grounded in audience research and supported by real-world fitness app statistics, providing a robust, data-driven foundation for both UX and full-stack implementation.

### Profile Management

**Goal Alignment**: "User-Friendly Navigation" & "Personalization and Control"  
**Stat Support**: 72% of users prefer personalized fitness plans

- As a **new user**, I want guided account creation so I can start my fitness journey without confusion.
- As a **returning user**, I want to log in securely using email or username across devices.
- As an **experienced user**, I want to update my name and bio to reflect my fitness evolution.
- As a **visual user**, I want to upload a profile picture with preview for a more personal experience.

### 🏋️ Training Guidance

**Goal Alignment**: "Structured Training" & "Personalization"  
**Stat Support**: Structured guidance increases retention by 75%

- As a **beginner**, I want clear explanations of workouts so I can train confidently.
- As an **intermediate user**, I want access to progressive plans that match my goals.
- As an **advanced user**, I want detailed breakdowns of muscle groups and techniques.
- As a **goal-setter**, I want training plans tailored to strength, endurance, or hypertrophy.

### Activity Tracking

**Goal Alignment**: "Motivation through Progress" & "User Engagement"  
**Stat Support**: Daily tracking users are 2x more likely to hit goals

- As a **consistency-focused user**, I want to track my activity with simple visuals to build habits.
- As a **motivated user**, I want to log completed workouts and view my activity history.
- As a **data-driven user**, I want to earn milestones and see trends that keep me engaged.

### Progress & Insights

**Goal Alignment**: "Progress Tracking" & "Data-Driven Feedback"  
**Stat Support**: 68% retention for self-monitoring users (vs. 32% non-tracking)

- As a **goal-oriented user**, I want to set SMART goals with built-in progress tracking.
- As a **self-improver**, I want visual analytics to review my strengths and weaknesses.
- As a **strategic user**, I want actionable insights that help refine my routine.

### Settings & Account Management

**Goal Alignment**: "Privacy by Design" & "Mobile Accessibility"  
**Stat Support**: 92% of users access fitness platforms via smartphone

- As a **privacy-conscious user**, I want to permanently delete my account with clear confirmation.
- As a **mobile-first user**, I want a responsive settings page I can manage on the go.
- As a **customization-focused user**, I want control over personal preferences and app experience.

### Why These Stories Matter

Each story targets a documented user need or pain point:

- **Retention-Driven Onboarding**: 25% of users abandon fitness apps after one session. Our profile and training flows are designed to reduce friction and improve first-use success.
- **Personalized Fitness**: 72% of users want tailored plans—addressed through editable profiles, goal-oriented plans, and adaptive guidance.
- **Mobile Optimization**: With 92% of fitness app traffic from mobile, every feature is designed responsively with intuitive navigation.

### Implementation Framework

Each user story maps directly to development tasks and UI logic—bridging the gap between user expectations and technical implementation. These stories inform:

- Component structure
- Backend endpoints
- Validation rules
- Testing priorities
- Success metrics

This structured, user-centric approach ensures every feature is purpose-built to solve a real problem or meet a validated goal.

### From Stories to Strategy

These stories aren't hypothetical—they're backed by measurable industry insights and behavioral trends. Each decision was guided by real data to ensure that Forge Fitness not only meets user expectations but competes at the highest standard.

The following section presents key statistics and market validation that shaped the product roadmap—from onboarding to engagement and long-term retention.

---

## Statistics  

The following **market research** and **user behavior data** have been carefully selected to inform the **development decisions** for Forge Fitness. These insights highlight **key trends** in **fitness app user engagement**, **activity tracking habits**, and **personalized goal-setting preferences**.  

Each metric provides **valuable insights** that guide the **app’s feature priorities** and **implementation approach**, ensuring the application meets **real user needs** while maintaining **modern UX/UI and development practices**. The data is categorized into **four core focus areas** that align with **Forge Fitness objectives**:  

### **1. User Engagement & Retention**   
- **Key Insight:** A significant percentage of **fitness app users** abandon apps after the **first use**. However, apps with **structured goal-setting, progress tracking, and intuitive navigation** see **higher retention rates**.  
- **Supporting Data:**  
  - 📉 **25% of fitness app users** stop using the app after a **single session**.  
  - 📈 **Retention-focused features**, such as **personalized goals, achievement tracking, and structured workouts**, help **retain over 75%** of users.  

**🔹 How Forge Fitness Addresses This:**  
✔ **Clear onboarding & navigation** – The **Dashboard** simplifies access to **all sections** for **seamless user flow**.  
✔ **Goal-based motivation** – The **Progression Page** keeps users engaged by offering **milestones, progress tracking, and feedback loops**.  
✔ **Consistent engagement tools** – The **Activity Page** tracks **daily movement**, making fitness tracking a **daily habit**.  

**📊 Visual Representation:**  
![User Engagement Chart](assets/images/charts/piechart.png)  

**🔗 Supporting Data:** [In-App Engagement Statistics & Tips for Health Apps](https://www.storyly.io/post/statistics-tips-for-health-apps-in-app-engagement)  

---

### **I. Activity Tracking & User Behavior**   

- **Key Insight:** Users who engage with **daily activity tracking** are more likely to **achieve fitness goals** and **retain long-term app usage**.  
- **Supporting Data:**  
  - **80% of engaged users** actively track **workouts, steps, and calories** within their fitness apps.  
  - **Daily tracking users** are **2x more likely** to stay engaged in their **fitness journey** compared to users who don’t track progress.  

**🔹 How Forge Fitness Addresses This:**  
✔ **Daily Activity Tracking** – The **Activity Page** allows users to **log steps, calories burned, and workouts** to maintain consistency.  
✔ **Workout Logging & Summaries** – The **Training Section** provides structured **workout logs and plans** for better tracking.  
✔ **Instant Feedback & Insights** – The **Progression Page** helps users **visualize trends** and **adjust their routines accordingly**.  

---

### **II. Personalization & Goal-Driven Features**  
- **Key Insight:** Apps that offer **personalized fitness plans** and **adaptive goal-setting** see a **higher completion rate** for user fitness programs.  
- **Supporting Data:**  
  - **72% of users** prefer apps that allow them to **customize training plans** and set **individualized milestones**.  
  - Users with **personalized progress tracking** are **50% more likely** to **consistently achieve fitness goals**.  

**🔹 How Forge Fitness Addresses This:**  
✔ **Goal Setting & Milestones** – The **Progression Page** allows users to **define and track short-term and long-term fitness goals**.  
✔ **Customizable Workouts** – The **Training Page** offers structured and **adaptable plans** for different fitness levels.  
✔ **User Feedback & Adjustments** – The **Settings Page** enables users to **modify their preferences**, keeping the experience tailored.  

---

By leveraging these **core insights**, Forge Fitness ensures its features align with **proven engagement models**, **data-driven personalization**, and **seamless user experiences**—making it an **effective and intuitive fitness application** for all users.  

---

### 2. **Fitness App Market Trends**  

- **Market Size & Growth:**  
  - The **global fitness app market** is projected to grow from **USD 14.7 billion (2023) to USD 120.37 billion by 2030**, reflecting a **CAGR of 17.6%**.  
  - The rapid adoption of **fitness technology** and **AI-driven personalization** is driving market expansion.  
  - **Hybrid fitness models** (combining in-app training with real-world activities) are becoming increasingly popular.  

**📊 Visual Representation:**  
  ![Graph](assets/images/charts/graphchart.png)

- **Source**: [Grand View Research](https://www.grandviewresearch.com/industry-analysis/fitness-app-market)

---

#### **Key Market Trends & How Forge Fitness Aligns**  

✅ **Personalization & AI-Driven Insights**  
- **72% of fitness app users** prefer **personalized workout recommendations** and **goal-based tracking**.  
- 🔹 **Forge Fitness Solution:** The **Training & Progression Pages** provide structured **goal-setting, tracking, and adaptive insights**.  

✅ **User Engagement via Gamification & Achievements**  
- **60% of fitness app users** stay engaged **longer** when apps include **progress tracking & achievements**.  
- 🔹 **Forge Fitness Solution:** The **Achievements Section** in the **Activity Page** encourages **streaks, milestones, and personal records** to keep users motivated.  

✅ **Mobile-First Approach & Accessibility**  
- **92% of fitness app users** primarily use **smartphones**, making mobile-first design **a necessity**.  
- 🔹 **Forge Fitness Solution:** The app is designed with **a responsive layout**, **touch-friendly elements**, and **an intuitive dashboard** for seamless navigation.  

✅ **Demand for Quick & Efficient Workouts**  
- **Over 50% of users** prefer fitness apps that offer **time-efficient workouts**.  
- 🔹 **Forge Fitness Solution:** The **Training Section** offers **structured plans & quick workout logging** to fit busy lifestyles.  

---

### **Relevance to Forge Fitness**  

The **growth of the fitness app market** and **emerging user preferences** support the **development direction of Forge Fitness**:  
✔ **User-Centric Features:** Personalized fitness tracking & adaptive workouts.  
✔ **Engagement Strategies:** Gamification through achievements & progress tracking.  
✔ **Mobile Optimization:** Seamless experience across **devices & screen sizes**.  

By aligning with **key industry trends**, Forge Fitness ensures **long-term usability, engagement, and innovation** in the competitive fitness app space.  

---

### 3. **User Health Habits**:

- **Key Statistics:**  
  - 📈 **68% retention rate** at 12 months for users who actively **self-monitor** vs **32% for non-monitoring users**.  
  - 🔄 **Weekly active users** show **82% higher retention rates** compared to sporadic users.  
  - 📊 **Multi-feature users** demonstrate **40% higher daily usage rates**.  
  - ⏰ **Personalized reminders** increase app interaction by **25%**.  

**📊 Visual Representation:**  
![Bar Chart](assets/images/charts/barchart.png)  

**🔗 Source:** [Effect of Self-Monitoring on Fitness Adherence](https://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0201166)  

---

### **How Forge Fitness Addresses This:**  

✅ **Comprehensive Tracking Integration**  
- 🏃‍♂️ **Daily Activity Logging** – Users can learn how to **track workouts, steps, calories burned, and active time** through the **Activity Page**.    
- 🏅 **Achievement Milestones** – The **Achievements Section** motivates users with **streaks, personal bests, and completion badges**.  
- ⏰ **Personalized Goal Reminders** – Users receive **activity prompts & goal reminders** to stay engaged with their fitness journey.  


This structured **demonstration-based approach** ensures that users understand **how to track progress, set goals, and interpret fitness data**—without requiring real-time integrations.

---

### 4. **Mobile-First Design Importance**:

- **Key Statistics**:  

  - **Mobile Dominance**:  
    - Over **54% of global web traffic** comes from mobile devices as of **2024**.  
    - _Source_: [Statista: Share of Website Traffic from Mobile Devices](https://www.statista.com/statistics/277125/share-of-website-traffic-coming-from-mobile-devices/)  

  - **User Preferences for Mobile Apps**:  
    - **85% of users** prefer mobile apps over websites due to their **speed, convenience, and accessibility**.  
    - _Source_: [App Usage Statistics 2024](https://www.statista.com/topics/1002/mobile-app-usage/)  

  - **Fitness App Users are Mobile-Centric**:  
    - **92% of fitness app users** access these apps via their smartphones, making **mobile design crucial**.  
    - _Source_: [Mobile App Usage Statistics for Fitness Apps](https://www.businessofapps.com/data/fitness-app-market/)  

  - **Responsive Design Increases Retention**:  
    - Apps with **seamless mobile experiences** have **30% higher retention rates** compared to non-mobile-optimized platforms.  
    - _Source_: [UX Design and Retention Study](https://www.uxdesigninstitute.com/blog/app-usage-statistics/)  

📊 **Visual Representation:**  
![Horizontal Bar Chart](assets/images/charts/horizontal-barchart.png)  

---

### **🔹 How Forge Fitness Addresses This:**  

✅ **Mobile-Friendly UI & Navigation**  
- 📱 **Responsive Layout** – The **Dashboard** is structured for **easy navigation across all screen sizes**, ensuring a **smooth user experience on mobile devices**.  
- 🎯 **Touch-Friendly Interactions** – Buttons, forms, and key **action elements are designed for mobile usability** with intuitive tap-based interactions.  
- 📌 **Simplified Content Structure** – Each page provides **clear sections** that allow users to quickly understand **how fitness tracking works**.  

✅ **Optimized Feature Display for Mobile Users**  
- 🏋️‍♂️ **Training Section** – Structured **workout plans and demonstrations** are presented in a **mobile-friendly** format.  
- 📊 **Progression Page** – Displays **goal-setting concepts, performance tracking, and feedback** in a way that is **accessible and easy to follow**.  
- ⚙️ **Settings Page** – Users can learn how to **manage their account, feedback, and app settings** in a **streamlined** mobile layout.  

✅ **User Experience Benefits**  
- 🚀 **Efficient Navigation** – Users can move seamlessly between sections without confusion.  
- 🔍 **Clear Visual Cues** – Icons and **concise explanations** ensure users understand **how each feature works**.  
- 📖 **Educational Approach** – Instead of **real-time tracking**, the app **demonstrates best practices for fitness monitoring** through well-structured UI components.  

---

### **📌 Summary of Statistics & Design Choices**  

Market research strongly supports the **mobile-first approach** taken in Forge Fitness. With **fitness apps projected to reach $120.37 billion by 2030**, the importance of **accessible and intuitive mobile interfaces** continues to grow. The statistics confirm that **92% of fitness app users** prefer **smartphone-based platforms**, reinforcing the decision to **prioritize responsive UI/UX principles** in this project.  

By integrating these **data-driven design decisions**, Forge Fitness offers **a structured and user-friendly demonstration of fitness tracking methodologies**, ensuring users **learn how to manage their fitness journey effectively**—without requiring **real-time tracking capabilities**. 🚀  

---

## Initial Design

The visual identity of Forge Fitness is built on a carefully selected **color palette** that emphasizes clarity, professionalism, and user engagement. The combination of light and complementary colors creates a **modern aesthetic** that enhances readability while maintaining a strong visual hierarchy.

### Color Scheme

![Colour Scheme](<assets/images/colour-scheme/forge_fitness-colour scheme.png>)

| Color  | Name                  | Usage |
|--------|-----------------------|-------------------------------|
| `#66A3FD` | **Argentinian Blue** | Navigation bar |
| `#ECECEC` | **Anti-Flash White** | Body background |
| `#8CBCCA` | **Sky Blue**         | Buttons, Sections |
| `#1853AB` | **Sapphire Blue**    | Footer |

---

### Typography

The typography system leverages **Bootstrap's native font stack** with custom font weights and sizing for optimal readability and visual hierarchy:

| Element | Font Size | Font Weight | Usage | Responsive Adjustments |
|---------|-----------|-------------|-------|----------------------|
| **Header Title** | `1.8rem` | `700` (Bold) | Main navigation branding | `1.4rem` on mobile |
| **Welcome Card Heading** | `fs-3` class | `600` (Semi-bold) | Hero section titles | `1.5rem` on mobile |
| **Auth Page Title** | `2rem` | `700` (Bold) | Login/Signup headings | `1.7rem` mobile, `1.5rem` small mobile |
| **Action Card Icons** | `fs-1` class | Default | Dashboard navigation | `1.8rem` on mobile |
| **Form Labels** | `0.9rem` | `600` (Semi-bold) | Form field labels | Consistent across devices |
| **Form Inputs** | `1rem` | `400` (Regular) | Input fields and text areas | `0.95rem` mobile, `0.9rem` small mobile |
| **Button Text** | `1rem` | `600` (Semi-bold) | Primary action buttons | `0.95rem` mobile, `0.9rem` small mobile |
| **Footer Text** | `0.95rem` | `500` (Medium) | Footer links and copyright | `0.85rem` mobile, `0.8rem` small mobile |
| **Badge Text** | `0.75rem` | Default | Status indicators | Consistent across devices |
| **Help Text** | `0.85rem` | Default | Form assistance text | `0.8rem` mobile, `0.75rem` small mobile |

#### **Typography Features**

| Feature | Implementation | Purpose |
|---------|---------------|---------|
| **Text Shadows** | `1px 1px 2px rgba(255, 255, 255, 0.9)` | Enhanced readability on gradient backgrounds |
| **Letter Spacing** | `-0.5px` on auth titles | Improved visual balance for larger headings |
| **Line Height** | `1.5` for form elements | Optimal reading comfort and touch targets |
| **Font Stack** | Bootstrap system fonts | Cross-platform compatibility and performance |
| **Responsive Scaling** | Media query breakpoints | Optimal sizing across all devices |

#### **Iconography**
- **Bootstrap Icons**: Comprehensive icon system (`bi-` classes)
- **Consistent Sizing**: `fs-3`, `fs-4` classes for scalable implementation
- **Interactive States**: Hover effects with `transform: scale(1.1)` and color transitions

The typography system prioritizes **accessibility, performance, and visual consistency** while maintaining the professional fitness-focused aesthetic that defines the Forge Fitness brand.

---

## Wireframes

To create a top class fitness app, this website is being desinged with a great amount of care and attention to detail. In the Dashboard page, I have included a variety of features to help users create their own workout regimes and track their progress tailored to their fitness goals. Here are the main features down below:

## Dashboard page

![Dashboard](assets/wireframes/dashboard.png)

### 📌 Dashboard Overview

The **Dashboard Page** serves as the central hub for navigation, providing users with quick access to key sections of the Forge Fitness app. It ensures a **clean and intuitive layout**, making it easy for users to interact with various features.

---

### 🏠 **Navigation Bar**
- **Logout Button**: Securely sign out of the application at any time.

---

### 📂 **Main Sections**

- 👤 **Profile Section** - Allows users to **view and edit** their profile, update their **preferred name**, and add a **personalized bio** to tailor their fitness experience.

- 🏋️ **Training Section** - Provides access to **structured workouts and training plans**, helping users follow a fitness routine aligned with their **goals and fitness levels**.

- 🏃‍♂️ **Activity Section** - Enables users to **track daily activity**, including **workouts, logs, and achievements**, ensuring they can monitor their progress and stay motivated.

- 📈 **Progress Section** - Focuses on **self-review, feedback, and insights**, helping users analyze **performance trends, goal tracking, and long-term fitness improvements**.

- ⚙️ **Settings Section** - Grants access to **account management**, including **feedback submission, support options, and account deletion**, ensuring a user-controlled experience.

---

### 🔻 **Footer Features**
- 🌐 **Social Media Links**: Quick access to **Facebook, Instagram, Twitter, and YouTube** for fitness-related content and community engagement.
- 🔗 **Footer Navigation**: Provides persistent **access to key sections**, ensuring seamless user experience across the app.


---

## Sign Up page

![Sign up](assets/wireframes/signup.png)

The sign up interface provides a streamlined onboarding experience while capturing essential user information. Key features include:

### Design Elements

- Modern, clean layout with clear visual hierarchy
- Enticing opening message to encourage sign-up
- Responsive form design optimized for all devices
- Consistent brand colors using the established palette

### Core Functionality

- Required profile information fields (name, email, password)
- Password visibility toggle for password field

---

## Login Page

![Login](assets/wireframes/login.png)

The **Login Page** provides users with a simple and secure authentication interface, ensuring quick and easy access to the Forge Fitness platform. The design prioritizes usability and accessibility while maintaining a clean, minimalist layout.  

---

### **Design Elements**  

- **Minimalist layout** focusing on essential login components.  
- **Responsive form design** that adapts to all screen sizes.  
- **Brand-consistent typography and colors**, ensuring visual coherence.  
- **Clear and accessible form fields** for easy user interaction.  

---

### **Core Functionality**  

- **Email or Username Authentication**  
  - Users can log in using their **registered email or username**.  

- **Password Input with Toggle Visibility**  
  - A **"Show Password"** option allows users to toggle password visibility for ease of entry.  

- **Persistent Login Option**  
  - The **"Keep me logged in"** checkbox enables users to stay signed in across sessions.  

- **Forgot Password Recovery**  
  - A **"Forgot password?"** link provides users with a direct way to reset their credentials.  

- **New Account Registration Link**  
  - A **"Create an account"** link encourages new users to sign up seamlessly.  

---

### **User Experience**  

- **Simple, intuitive input fields** for easy login.  
- **Streamlined navigation** with clear sign-up and password recovery options.  
- **Secure session handling** to protect user credentials.  
- **Mobile-friendly layout**, ensuring accessibility across all devices.  

---

### **Why This Page Matters**  

The **Login Page** serves as the gateway to the Forge Fitness platform, offering a **seamless and user-friendly authentication experience**. By maintaining **strong security measures and a clean, intuitive layout**, it ensures a **smooth onboarding process** for both new and returning users.  

---

## Profile Page

![Profile](assets/wireframes/profile-page.png)

The **Profile Page** allows users to personalize their fitness experience by managing their profile details. With a clean and structured layout, users can easily update their information, add a profile photo, and provide a short bio.  

### Design Elements

- Clean, modern layout with clear section divisions for easy navigation
- Interactive elements like buttons and input fields for user customization
- Consistent color scheme and typography aligned with the Forge Fitness brand
- Large, user-friendly **"Upload Photo"** option for profile personalization
- Responsive design ensuring seamless access across devices

### **Design Elements**  

- **Minimalist and intuitive layout** for easy profile customization.  
- **User-friendly input fields** for quick data entry and updates.  
- **Consistent color scheme and typography** aligned with Forge Fitness branding.  
- **Large and accessible "Upload Photo" button** for seamless profile personalization.  
- **Fully responsive design**, ensuring accessibility across different devices.  

---

### **Core Functionality**  

- **Profile Customization**  
  - Users can enter a **preferred name** to personalize their profile.  
  - A **bio/about me section** lets users add a short description about themselves.  

- **Photo Management**  
  - Upload a **profile photo** to personalize the user profile.  
  - Supports common image formats such as **PNG and JPEG**.  
  - Option to **update or remove the profile picture** if needed.  

- **Save Changes**  
  - Users can **save profile updates** to ensure all modifications are stored.  
  - A simple **confirmation process** ensures that changes are reflected instantly.  

---

### **User Experience**  

- **Simple and intuitive input fields** for quick profile updates.  
- **Seamless user interactions**, ensuring effortless navigation.  
- **Visual feedback** when changes are successfully saved.  
- **Responsive layout**, allowing smooth access on different screen sizes.  

---

## Training Page

![Training Page](<assets/wireframes/training section.png>)

The **Training Page** serves as a central hub for users to explore structured workout guidance and how personalized fitness plans work. This section is designed to provide clear, actionable insights, making it easier for users to understand their training options and track progress efficiently.

### **Introduction**

The **Introduction** section provides users with a foundational understanding of the training program. It explains the core principles behind structured fitness routines and highlights the importance of consistency, form, and goal setting. Whether users are beginners or experienced athletes, this section offers essential guidance on how to approach their fitness journey effectively.

### **Workouts**

The **Workouts** section is dedicated to helping users understand the role of different muscle groups and the exercises that target them effectively. 

- **Muscle Group Breakdown:**
  - Users can explore all the workout categories based on different body areas, ensuring a balanced workout approach.
  - Includes guidance on exercises for major muscle groups such as:
    - Chest
    - Back
    - Legs
    - Shoulders
    - Arms
    - Core
    - Full Body Workouts

- **Exercise Demonstrations:**
  - Each workout category provides information on the most effective exercises for that muscle group.
  - Users can follow step-by-step instructions or access additional resources to ensure proper form and injury prevention.

- **Training Techniques:**
  - Guidance on how to integrate progressive overload, rest periods, and rep schemes into their routine for optimal results.

### **Training Plans**

The **Training Plans** section provides structured workout programs tailored to different fitness goals. Whether users are looking to **lose weight, build muscle, or enhance endurance**, this section offers a variety of programs to suit their needs.

- **Structured Programs:**
  - Users can follow pre-designed training plans or customize their own based on their fitness level and goals.
  - Each plan outlines:
    - Recommended workout frequency
    - Exercise selection
    - Progress tracking strategies

- **Goal-Based Training Plans:**
  - **Weight Loss:** Focused on high-intensity workouts, calorie burning, and metabolic conditioning.
  - **Muscle Gain:** Strength-building exercises, hypertrophy-focused routines, and recovery strategies.
  - **Endurance Training:** Plans designed to improve stamina, cardiovascular health, and athletic performance.

- **Progress Tracking:**
  - Encourages users to log their workouts and adjust their plans based on improvements and feedback.

### **Summary**

The **Summary** section ties together key takeaways from the **Introduction, Workouts, and Training Plans**. This section reinforces how users can apply the provided information to their fitness journey, ensuring they make informed decisions that align with their personal health goals.

- **Why This Matters:**
  - Highlights how structured training enhances results.
  - Emphasizes the importance of tracking progress and making adjustments.

- **Next Steps:**
  - Encourages users to explore different training plans, experiment with workout variations, and stay consistent in their routines.
  - Provides recommendations for further learning and improvement.

### **Training Page Conclusion**

The Training section of the platform is designed to offer a **comprehensive, structured, and user-friendly** approach to fitness. By combining key insights from **Introduction, Workouts, Training Plans, and Summary**, users are empowered with the knowledge and resources they need to take control of their fitness journey. Whether they are starting out or refining their routine, this section provides the **guidance, structure, and motivation** needed to achieve long-term success.

---

## Activity Page

The **Activity Page** provides users with a centralized space to learn about their **daily movement, workout progress, and fitness milestones**. Designed with a structured layout, it ensures that users can quickly access key fitness insights on a **single page** without navigating through multiple sections. This streamlined approach enhances usability, making it easier to stay engaged and track progress effectively.

![Activity Page](assets/wireframes/activity-section.png)

---

## **Page Structure and Purpose**

The Activity Page is structured into four main sections, each focusing on a different aspect of fitness tracking. These sections work together to provide a **comprehensive snapshot** of the user’s understanding about daily and long-term activity.

### **Introduction**  
The **Introduction** section sets the foundation for understanding activity tracking. It highlights the significance of **monitoring both daily movement and structured workouts**, emphasizing how an active lifestyle contributes to overall fitness goals.  
- Encourages users to view movement beyond workouts, incorporating **everyday activity** as part of their progress.  
- Reinforces the importance of tracking **steps, calories burned, and overall consistency** to build long-term fitness habits.  

---

### **Daily Activity**  
The **Daily Activity** section provides users with a summary of their movement patterns throughout the day, giving them insight into how **active or inactive** they have been.  
- Displays **steps taken, active vs. inactive calorie burn, and general activity trends** in an easy-to-read format.  
- Helps users recognize patterns in their daily routine, allowing them to make **healthier lifestyle adjustments**.  
- Encourages consistency by showing users how **small daily movements contribute to their bigger fitness goals**.  

This section is designed for users who want to **stay mindful of their daily habits**, ensuring that they maintain steady progress even outside of structured workouts.

---

### **Workout Tracking**  
The **Workout Tracking** section focuses on users completed workouts, serving as a quick reference point for reviewing their fitness journey.  
- Summarizes the **type, frequency, and duration** of recent workouts.  
- Provides an **overview of workout patterns** to help users assess consistency and performance.  
- Encourages users to **reflect on their training routines** and stay committed to their goals.  

By having **workout data available at a glance**, users can **stay accountable** and ensure that they are following a balanced training plan.

---

### **Achievements**  
The **Achievements** section highlights key fitness milestones and accomplishments, reinforcing motivation and long-term engagement.  
- Recognizes **streaks, personal bests, and consistency milestones** to celebrate user progress.  
- Encourages a **sense of accomplishment** by visually showcasing fitness achievements.  
- Helps users **set new goals** based on past performance.  

By rewarding progress, this section provides users with **a continuous source of motivation** to push further and maintain their fitness routine.

---

### **Key Benefits of the Activity Page**

The **Activity Page** is designed to enhance user engagement by providing a **structured and accessible** way to monitor fitness progress.  

### **Why This Page Matters:**
✔ **Single-Page Overview:** Eliminates unnecessary navigation, making fitness tracking more intuitive.  
✔ **Data-Driven Insights:** Helps users make informed decisions about their activity levels and workout habits.  
✔ **Consistency & Motivation:** Encourages ongoing progress by reinforcing positive behavior and achievements.  
✔ **Improved Accountability:** Allows users to track their own patterns, adjust their routines, and stay committed to their fitness goals.  

---

### **Activity Page Summary**  

The **Activity Page** is a streamlined solution for users who want **clear, organized, and accessible fitness tracking** in one place. By integrating **Daily Activity, Workout Tracking, and Achievements**, this page empowers users to **stay consistent, celebrate their progress, and build sustainable fitness habits** over time.

---


## Progression page

The **Progression Page** provides users with a structured and intuitive platform to **track their fitness journey** over time. By focusing on **goal setting, performance tracking, and personalized feedback**, this page helps users learn how to stay motivated, recognize progress, and make informed adjustments to their fitness routines.  

![Progression](<assets/wireframes/progression .png>)

---

### **Features and Sections**  

### **1. Goal Setting / Milestones**  
**Define your fitness goals and stay on track**  

This section helps users how to establish **short-term and long-term fitness goals** while tracking their progress toward meaningful milestones.  

- Set **personalized goals** based on your fitness objectives (e.g., weight loss, muscle gain, endurance improvement).  
- Monitor your **goal completion percentage**, giving you a clear sense of progress.  
- Celebrate **milestones and achievements**, such as reaching a strength PR, improving running speed, or completing a workout streak.  

📌 **How to Use This Section Effectively:**  
✔ Clearly define measurable goals (e.g., "Lose 5kg in 3 months" or "Run 10km without stopping").  
✔ Regularly check your milestone progress to stay motivated.  
✔ Adjust goals as needed to **continue pushing toward new challenges**.  

---

### **2. Performance Tracking**  
**Analyze your trends and measure real progress**  

Tracking **performance metrics** over time helps users understand their **strengths, weaknesses, and areas for improvement**.  

- View **progress summaries** that reflect workout consistency, strength development, endurance gains, and more.  
- Identify **patterns in fitness habits** through structured data representation.  
- Compare past and present performance to **track improvements** and optimize training.  

📌 **How to Use This Section Effectively:**  
✔ Regularly review your progress summaries to assess improvements.  
✔ Use historical performance data to adjust workout intensity and frequency.  
✔ Identify trends that may indicate the need for recovery or workout variations.  

---

### **3. Feedback and Insights**  
**Refine your training with meaningful insights**  

This section provides **personalized guidance** based on user activity and progression trends, helping users stay engaged and make strategic adjustments.  

- Gain **data-driven insights** into your progress and performance consistency.  
- Receive **motivational feedback**, such as reminders to stay consistent, recovery recommendations, or milestone celebrations.  
- Learn how to **optimize workouts** based on training data, ensuring **continuous improvement**.  

📌 **How to Use This Section Effectively:**  
✔ Reflect on feedback to make **targeted adjustments** to training plans.  
✔ Use progress insights to **fine-tune your workout intensity, recovery schedule, and goal-setting approach**.  
✔ Stay motivated by celebrating milestones and acknowledging improvements in strength, endurance, and consistency.  

---

## **Why the Progression Page is Essential**  

The **Progression Page** serves as a **central hub** for tracking progress, celebrating achievements, and making strategic adjustments to training plans. By combining **goal tracking, performance analysis, and feedback-driven improvements**, users can ensure **consistent growth and long-term success** in their fitness journey.  

✔ **Set clear goals and track milestone achievements.**  
✔ **Analyze performance trends to optimize training.**  
✔ **Use feedback to make data-driven adjustments for continuous progress.**  

By regularly engaging with this page, users will gain the knowledge to **stay accountable, make informed training decisions, and maintain long-term motivation** toward achieving their fitness goals. 🚀  

---

### Settings Page

![Settings](<assets/wireframes/settings .png>)

The **Settings Page** provides users with a simple yet essential option to manage their account. This page ensures users have full control over their presence on the platform by offering a straightforward way to remove their account if needed.  

### **Delete Account**  
Users who wish to permanently remove their account can do so from this section.  
- **Irreversible Action:** Deleting an account will erase all associated data and cannot be undone.  
- **User Control:** Ensures users have complete authority over their data and app presence.  
- **Final Confirmation:** Before proceeding, users are encouraged to carefully consider their decision.  

By keeping the **Settings Page minimal**, the app maintains a **clean and straightforward experience**, allowing users to focus on their fitness journey without unnecessary complexity.  

---

## User Experience | Final Design 
 
The final design of Forge Fitness builds upon the original UX plan and wireframes by refining user flows, improving layout structure, and incorporating meaningful feedback based on real-world user interaction patterns. While the initial concept prioritised clarity and responsiveness, the implemented version elevates this by delivering a more intuitive navigation system, a clean dashboard experience, and clearly segmented modules for training and activity tracking. Key areas—such as the training planner, activity log, and profile editor—have evolved to be more accessible, interactive, and visually distinct, ensuring that users can manage their fitness goals with minimal friction. Compared to the scoped wireframes, the final product introduces stronger contrast, smoother transitions between pages, and a more cohesive visual hierarchy, resulting in a user interface that is not only functional but highly engaging across devices.

To see the final designs on the dashboard, training, activity, progress and settings pages. Please sign up and by here and look 
at what they have to offer - [Sign up](https://forge-fitness-d9cu.onrender.com/signup/)

## Dashboard Overview

[View Live](https://forge-fitness-d9cu.onrender.com/dashboard/)

The final implementation of the Dashboard Page acts as the launchpad for user interaction across Forge Fitness. It has evolved significantly from the original wireframe to deliver a visually engaging, responsive, and functionally rich experience. The page balances aesthetics with usability, employing a clean card-based grid layout, subtle animations, and consistent iconography to guide the user intuitively across the app's core modules. It places the user at the centre of their fitness journey, offering clear pathways to manage progress, plans, and personalisation without cognitive friction.

## 🏠 Navigation Bar

The navigation bar is fixed at the top of the screen and serves as the primary anchor for user orientation and flow:

- Clearly labelled links to Dashboard, Training, Activity, Profile, and Settings
- Active state indicator (e.g. underline) for the current page
- Secure Logout button available on all pages
- Responsive behaviour ensures the navbar collapses cleanly on mobile devices for optimal readability and access

### 📂 Interactive Dashboard Grid

The main content is composed of five interactive section cards, each styled with consistent hover states, iconography, and spacing to aid recognition and improve scanability. Each card directs the user to a core module:

### 👤 Profile
- View and update personal details such as display name and bio
- Reinforces the app's personalised nature and gives the user control over their representation

### 🏋️ Training
- Gateway to curated training plans and workouts
- Empowers users to follow structured routines based on their fitness goals

### 🏃‍♂️ Activity
- Track completed workouts and review logged notes
- Central to helping users reflect, log improvements, and stay consistent

### 📈 Progression
- Visual progress insights and performance tracking
- Though the original wireframe envisioned basic summaries, the final design elevates this with custom chart graphics to better engage users and encourage reflection

### ⚙️ Settings
- Manage account preferences, including support options and the ability to submit feedback or delete the account
- Emphasises user autonomy and GDPR-conscious design

### 🎨 Visual & UX Enhancements

Compared to the scoped wireframe, the final version features several key improvements:

- **Stronger visual hierarchy** with bold headers, card spacing, and icon usage for at-a-glance understanding
- **Consistent colour scheme** drawn from the site's style guide (header/footer/button colours)
- **Hover animations** provide instant interaction feedback, enhancing responsiveness
- **Fully mobile-responsive layout**, with each card stacking elegantly for smaller screens
- **Chart areas** use image placeholders with a consistent visual theme across all chart types, hinting at future dynamic data integration

## 🔻 Footer Area

The footer remains minimalistic to avoid visual clutter on key landing pages:

- Present on all pages for brand consistency
- Space reserved for future enhancements such as social media links or partner content

---

## Sign Up Page | Final Design

🔗 [View Live](https://forge-fitness-d9cu.onrender.com/signup/)

The Sign Up Page in the final design delivers a frictionless onboarding experience with a focus on clarity, visual appeal, and responsive behaviour. Expanding on the original plan, the implemented version introduces subtle UX enhancements and clean form validation to guide users through the registration process confidently.

### 🎨 Design Elements

- **Sleek, brand-aligned layout** with generous spacing and soft shadow accents to elevate form prominence
- **Concise, motivational welcome message** reinforces value and encourages conversion
- **Fully responsive form**, ensuring usability across mobile, tablet, and desktop screens
- **Clear visual feedback** for input focus and error states enhances user trust and interaction clarity
- **Brand colour palette** is consistently applied to buttons, links, and headings for a cohesive experience

### 🔐 Core Functionality

- **Collects essential user data**: username, email, password
- **Real-time password confirmation matching** to avoid errors during submission
- **Password visibility toggle** ensures users can verify input securely
- **Call-to-action footer links** offer easy redirection to login for returning users

### 📱 User Experience Highlights

- **Simple, vertically stacked layout** reduces visual complexity and supports thumb-friendly mobile use
- **Error messages and success states** are styled clearly, ensuring immediate feedback during registration attempts
- **Auto-focus and tab-order** optimise keyboard navigation for accessibility

### 🧭 Why This Page Matters

As the primary entry point for new users, the Sign Up page balances efficiency and reassurance. By minimising friction, maintaining clean visual flow, and offering clear interaction cues, the page boosts user confidence from the moment they begin their fitness journey with Forge Fitness.

---

## Login Page | Final Design

🔗 [View Live](https://forge-fitness-d9cu.onrender.com/login/)

The Login Page in its final state has been refined to offer users a quick, secure, and intuitive authentication experience. Compared to the wireframe, the final build simplifies layout distractions, sharpens input visibility, and ensures a seamless flow for both desktop and mobile users.

### 🎨 Design Elements

- **Minimalist form structure**, centring user focus on login essentials
- **Responsively styled** to maintain usability across screen sizes and devices
- **Input fields provide subtle visual cues** (focus borders, spacing) for ease of interaction
- **Typography and button styles** follow the app's established visual identity, reinforcing brand trust

### 🔐 Core Functionality

- **Username or Email login support** for user flexibility
- **Password visibility toggle** improves input accuracy
- **"Remember Me" checkbox** allows users to persist their session securely
- **Forgot Password link** positioned logically for immediate recovery access
- **New user prompt** links directly to the Sign Up page

### 📱 User Experience Highlights

- **Clear call-to-actions** reduce decision fatigue for both new and returning users
- **Accessible form structure** with proper labels and feedback for keyboard/tab navigation
- **Secure form handling** ensures passwords and session data are protected

### 🧭 Why This Page Matters

Serving as the entry gate to the entire platform, the Login Page plays a vital role in shaping first impressions. With its clean presentation, fast performance, and user-focused features, it ensures returning users can access their fitness data efficiently while maintaining high standards of usability and trust.

---

## Profile Page – Final Design

**🔗 [View Live Profile Page](https://forge-fitness-d9cu.onrender.com/profile/)**  
**🔗 [View Live Edit Profile](https://forge-fitness-d9cu.onrender.com/profile/edit/)**

The final Profile Page offers users a personalised and accessible space to manage their fitness identity within Forge Fitness. Evolving from the original design, this section focuses on simplicity, responsiveness, and control, allowing users to update their display name and add a short bio that appears across key user-facing areas. While minimal by design, the profile area sets the foundation for future expansion such as photo uploads or social integration.

### 🎨 Design Elements

- **Clean, centred layout** with clear visual segmentation between Profile Info and Edit Actions
- **Typography and styling** remain consistent with the site-wide theme — crisp headings, soft card backgrounds, and well-aligned spacing
- **Subtle padding and box-shadow** enhance the form's visual hierarchy without creating clutter
- **Full mobile responsiveness** with input fields and buttons scaling appropriately for touch-based interfaces

### ✍️ Core Functionality

#### Profile Customisation
- **Preferred Name input** allows users to display a personalised identity rather than just their username
- **Bio/About Me section** lets users share brief personal info or motivational quotes — encouraging ownership over their fitness journey
- **Upload profile picture** allows users to personalise their profile with a photo

#### Save & Feedback
- **Clear "Save" button** confirms edits and updates the database in real time
- **Visual confirmation** ensures the user knows when changes have been successfully applied

### 📱 User Experience Highlights

- The **Edit Profile page** is intuitively structured, reducing user friction during updates
- **Input fields are auto-focused** and keyboard-accessible for efficient data entry
- **Error prevention through form validation** (e.g., required fields) ensures clean submissions
- **Feedback on successful changes** is immediate, with updates reflected directly on the Profile page

### 🧭 Why This Page Matters

The Profile Page plays a vital role in creating a sense of ownership for users. By giving them the ability to tailor how they appear within the app — even in a lightweight form — it supports the app's goal of fostering a personalised, motivating fitness environment. Its simplicity today lays the groundwork for future enhancements like profile photos, achievements, or activity summaries, without compromising the current user experience.

---

## Training Page | Final Design

**🔗 [View Live](https://forge-fitness-d9cu.onrender.com/training/)**

The Training Page is a comprehensive, user-centric resource designed to teach, inspire, and guide users through the fundamentals of effective training. In its final implementation, this page integrates interactive education, expert-led demonstrations, and a practical note-logging system — all aimed at helping users build a consistent, goal-driven fitness routine.

### Introduction Section

The page opens with a welcoming and motivational introduction that:

- Explains the importance of structure, consistency, and form in long-term fitness success
- Frames training as a skill to be developed, not just workouts to be completed
- Encourages users to approach fitness with purpose — not guesswork — regardless of experience level

### Workouts Section

This section is where theory meets application. It covers key muscle groups (Chest, Back, Legs, Shoulders, Arms, Core) and outlines recommended exercises — but more importantly, it enhances user learning with expert guidance from **Jeff Nippard**, a leading voice in evidence-based training.

### How Jeff Nippard's Content Enhances the Page:

- Each muscle group links to a dedicated Jeff Nippard YouTube video, curated to match the section's topic
- Topics include: Glute Training, Back Training, Shoulder Development, Core & Abs, Cardio, and more
- Each link is styled for accessibility and grouped clearly by training category

### Why Jeff Nippard?

Jeff Nippard's content has been selected as the gold standard for exercise demonstrations due to its strong scientific foundation, clear delivery, and practical focus. His videos offer a trusted, safe, and detailed reference for users looking to learn proper technique, avoid injury, and train efficiently. His influence directly shaped both the instructional tone and the structural flow of the workouts section.

A link to Jeff Nippard's full channel is provided for those who want to explore further beyond the scope of Forge Fitness.

### Training Plans Section

This section guides users in translating exercise knowledge into a sustainable training strategy. It includes:

- **Recommended splits** (e.g. 3, 4, or 5-day training weeks)
- **Goal-oriented programming:**
  - **Fat Loss:** High-volume, HIIT-style training
  - **Muscle Gain:** Hypertrophy, progressive overload
  - **Endurance:** Full-body circuits, cardio periodisation
- **Principles** on how to balance intensity, frequency, recovery, and progression

Plans are presented as flexible frameworks, not rigid programs — aligning with the app's goal of user empowerment and long-term adherence.

## Summary Section

This section condenses everything into practical takeaways:

### Key Themes: 
Structure, knowledge, habit-building

### Action Items:
- **This Week:** Choose a split, test workouts, start notes
- **This Month:** Track progression, review plans, adjust routines

Motivational messaging reminds users that "progress over perfection" is the key to momentum. It also transitions users naturally into the note-taking workflow.

### Training Notes – From Learning to Logging

The final component is a powerful, interactive Training Notes system, encouraging users to:

- **Create** custom notes for workouts, weekly plans, or personal reflections
- **Edit/update** logs as progress is made
- **Delete** irrelevant or outdated entries for clarity

Each note is tagged under the "Training" category, forming a chronological, user-controlled journal of progression — turning abstract fitness theory into measurable action.

### User Experience Highlights

- Fully responsive design with collapsible sections for ease of reading
- Colour-coded tabs and headings improve scanability
- Hover effects, CTA buttons, and layout spacing improve engagement
- Keyboard/tab navigation and high contrast support accessibility

### Acknowledging Jeff Nippard's Contribution

Much of the educational structure and video content in this section is based on the work of **Jeff Nippard**, whose science-based training resources serve as a foundation for safe, effective fitness guidance throughout this app. His content has been instrumental in shaping not just the instructional voice of the Workouts section, but also in influencing the prioritisation of form, injury prevention, and evidence-backed programming.

Full credit and thanks to Jeff Nippard – his channel remains one of the most trusted and educational platforms for anyone serious about training intelligently.

**🔗 [Visit Jeff Nippard's YouTube Channel](https://www.youtube.com/@JeffNippard)**

## Why This Page Matters

The Training Page brings together education, structure, and action. By blending reliable science (via Jeff Nippard), practical planning frameworks, and an interactive note system, it gives users everything they need to build — and stick to — a meaningful fitness journey. This section moves beyond basic fitness advice and instead empowers users with the knowledge and tools to train with clarity, purpose, and long-term sustainability.

---

## Activity Page | Final Design

**🔗 [View Live](https://forge-fitness-d9cu.onrender.com/activity/)**

The Activity Page brings a fresh, holistic approach to fitness tracking by focusing not only on workouts but on how users live throughout the entire day. Evolved from its original design as a simple tracker, it now serves as a 24-hour lifestyle dashboard, encouraging users to view movement, nutrition, habits, and health behaviours as interconnected elements of their overall fitness journey.

This page supports users in becoming more aware, more accountable, and more consistent — ultimately shifting their mindset from short workouts to long-term wellness.

### 🔄 Page Structure Overview

The page is structured into seven collapsible sections with a clear top navigation bar that allows users to jump between key themes:

- **Introduction**
- **Daily Activity**
- **Nutrition**
- **24-Hour View**
- **Tracking Methods**
- **Habit Building**
- **Summary + Notes**

The bottom of the page includes the **Health & Lifestyle Notes** section, which allows users to actively log their reflections, targets, or habit challenges — building self-awareness into actionable progress.

### 🧠 The 24-Hour Reality

This opening section challenges a common misconception: that gym time alone is enough. It introduces:

- **The "4.2% Trap"** – the reality that even 1 hour in the gym equals just 4.2% of a user's day
- **The "95.8% Solution"** – where real change happens: sleep, stress, food, hydration, and habits
- Encourages users to rethink how they measure progress and embrace their full daily routine as the arena for change

**Key takeaway**: "You cannot out-train a bad diet or poor lifestyle."

### 🚶 Daily Activity & Movement

This section explores non-exercise activity thermogenesis (NEAT) and the power of day-to-day movement:

**Tracks**: Steps, NEAT calories, movement patterns

- Differentiates between structured exercise and lifestyle activity (e.g. walking, cleaning, standing)
- Visual breakdowns encourage users to move more consistently — even outside the gym

**Highlights include**:
- Morning NEAT strategies
- Office NEAT (e.g., standing breaks)
- Evening activity suggestions

**✅ Activity Targets**:
- 8,000–12,000 steps/day
- 150+ active minutes/week
- Hourly movement breaks

### 🍎 Nutrition: The Foundation

This section reframes nutrition not as a diet, but as the core driver of results:

- Explains caloric balance (deficit, surplus, maintenance)
- Breaks down tracking methods: detailed (e.g. MyFitnessPal) vs. intuitive (e.g. hand portions)
- Emphasises common nutritional mistakes like:
  - "I'll just burn it off later"
  - Drinking your calories
  - Underestimating portion sizes

Users are provided with **Week-by-Week nutrition goals** to gradually build consistency.

### 🧬 Your 24-Hour Health Profile

This section ties it all together by giving users a complete picture of how sleep, stress, hydration, and habits impact results:

- Visual timeline of how users spend their 24 hours
- **Key lifestyle factors**:
  - 💤 Sleep Quality
  - 💧 Hydration
  - 💥 Stress Management
  - 🍎 Nutrition
  - 🕒 Screen time & recovery

This profile encourages users to see patterns, not just moments, and reinforces the power of small, daily actions.

### 📊 Holistic Tracking Methods

This section offers users a flexible framework to log and reflect on key behaviours:

- Encourages combining qualitative and quantitative tracking
- Promotes checklist habits, habit stacking, and journaling
- Explains the value of reflection, not just measurement

### 🔁 Building Lifestyle Habits

One of the most actionable areas of the page — this section empowers users to form habits with intention:

- **Habit Loop** (Cue → Routine → Reward)
- **Stacking strategies** (linking habits to routines)
- **2-minute rule** – start small, stay consistent
- **Environment design** – how to make good habits obvious and bad habits invisible

**It also addresses common blockers like**:
- "I don't have time"
- "I forget"
- "I'm inconsistent"

A **30-Day Habit Implementation Plan** is included to provide structure from Week 1 to Month 3.

### 🧾 Complete Health Summary

This final summary reinforces the most important principles:

**Big Picture View**: Health is determined by everything you do, not just workouts.

**Success Principles**:
- Focus on systems, not willpower
- Track small wins
- Build momentum slowly

**Action Plan**: A step-by-step system that covers:
- **Foundation** (Week 1–2)
- **Optimisation** (Month 2)
- **Mastery** (Month 3)

The closing call-to-action is clear: *"Start tracking your journey below — one note, one habit, one day at a time."*

### 📝 Health & Lifestyle Notes

Users can log lifestyle-specific reflections and goals:

- Add, edit, and delete notes focused on sleep, hydration, stress, nutrition, or habits
- Encouraged to write after each section for reflection or planning
- Fully responsive and styled consistently with the rest of the app

This feature transforms the Activity Page into a daily accountability system, not just a source of information.

### 💡 Why This Page Matters

The Activity Page transforms passive awareness into active ownership. It guides users to:

- Shift focus from workouts to total wellness
- Reflect daily with lifestyle notes
- Build sustainable health habits, not temporary routines

Whether someone is just starting their journey or refining their lifestyle, this page serves as a blueprint for lasting transformation — beyond the gym.

---

## Progression Page | Final Design

**🔗 [View Live](https://forge-fitness-d9cu.onrender.com/progression/)**

The Progression Page empowers users to take charge of their long-term fitness journey by tracking measurable goals, celebrating milestones, and reviewing real performance trends. It bridges the gap between daily activity and big-picture transformation by combining goal-setting tools, tracking frameworks, and motivational feedback — all within a structured and intuitive interface.

### 🔁 Page Structure Overview

The page is broken into five functional segments, each accessible through a tabbed navigation interface:

- **Foundation**
- **Goals**
- **Tracking**
- **Milestones**
- **Progression Notes**

Each section builds on the last, guiding users from understanding progress to acting on it. Collapsible cards enhance focus, while the visual style stays consistent with the wider Forge Fitness aesthetic.

### 💡 Foundation of Progress

This section introduces core training philosophy:

- **Direction Over Speed**: Prioritising consistency over intensity spikes
- **Measurable Growth**: Encourages tracking metrics that actually reflect improvement
- **Sustainable Systems**: Builds routines that work beyond motivation

**💬 Key Insight**: Progress is cyclical — users are reassured that plateaus are part of the process, not a sign of failure. The page builds trust by setting realistic expectations and shifting focus to long-term adherence.

### 🎯 Setting Meaningful Goals

This section teaches users to set smart, actionable fitness goals using the SMART framework:

#### Specific & Measurable:
- e.g. "Increase bench press by 20lbs"
- "Lose 2lbs/month for 6 months"

#### Achievable & Time-bound:
- Break large goals into 30, 60, or 90-day milestones

#### Types of goals covered:
- 💪 **Performance** (strength, endurance)
- ⚖️ **Body Composition** (weight, fat loss)
- ❤️ **Health Markers** (blood pressure, heart rate)
- 🔁 **Habit-Based** (consistency, lifestyle change)

#### ✅ Goal Examples Provided:
- **30-Day Goals**: "Walk 8,000 steps daily," "Complete 12 workouts this month"
- **90-Day Goals**: "Run a 5K," "Lose 8–12lbs," "Master 5 new exercises"

This section gives users the clarity and structure needed to turn aspirations into measurable outcomes.

### 📊 Performance Tracking

This section focuses on metrics that matter, helping users assess their actual progress with data:

#### Key Areas Tracked:
- 🔷 **Strength Progress** (weight lifted, reps/sets)
- 🟩 **Endurance Gains** (cardio duration, intensity)
- 🟨 **Consistency** (session frequency, streaks)

#### 📋 Simple Tracking Methods:
- Workout Logs
- Weekly Reviews
- Progress Photos
- Time Tracking (rest periods, time under tension)

**🚨 Note**: The guidance reminds users not to track everything, but to choose 3–5 key metrics aligned with their goals — making tracking sustainable and insightful rather than overwhelming.

### 🏅 Milestones & Breakthroughs

This section helps users visualise transformation and stay motivated through tangible wins:

#### Milestone Categories:
- 📆 **30-Day**: Build a habit, establish routine
- ⏳ **90-Day**: Improve body comp, consistency
- 🛠️ **1-Year**: Long-term transformation, advanced skill mastery

Users are taught to embrace plateaus, celebrate small wins, and make training adjustments (intensity, rest, variation) when needed.

**A central takeaway is reinforced:**
> **Consistency + Progressive Overload + Patience = Transformation**

This simple formula keeps users grounded and focused even when external results fluctuate.

### 📝 Progression Notes

Like Training and Activity notes, this section allows users to:

- Log specific fitness milestones
- Reflect on their goals, challenges, and breakthroughs
- Document mindset shifts (e.g. "Learned to embrace plateaus this week")
- Track performance weekly

A motivational prompt encourages users to:
- Set measurable targets
- Record small wins
- Reflect on their emotional and physical progress

This section supports the self-coaching mindset, helping users build ownership of their journey.

### 💡 Why This Page Matters

The Progression Page turns abstract growth into trackable, tangible progress. It combines educational content, tracking strategy, and self-reflection tools to:

- 📌 Help users set meaningful, attainable goals
- 📈 Teach them to track what matters and avoid burnout
- 🏆 Celebrate their progress and refine their plans

It's not just about "getting results" — it's about recognising them, adjusting the plan, and pushing forward with purpose.

Whether a user is starting fresh or breaking through a plateau, the Progression Page serves as a structured and supportive guide to sustainable, measurable transformation.

---

## Settings Page | Final Design

**🔗 [View Live](https://forge-fitness-d9cu.onrender.com/settings/)**

The Settings Page gives users essential control over their account with a minimal, purpose-driven layout. Designed with clarity and user autonomy in mind, it offers a secure, frictionless method for users to manage sensitive actions like account deletion — reinforcing transparency, privacy, and user empowerment throughout the Forge Fitness platform.

### ⚙️ Page Overview

Unlike other pages in the app that offer multiple layers of interaction, the Settings Page is intentionally simple and focused. It provides:

- **One clearly defined action**: Account Deletion
- **A single access point to Edit Profile**, redirecting users to their profile management section
- **A clean layout**, minimal distraction, and warning-heavy design to reinforce the gravity of the account deletion process

### 🧨 Delete Account – Secure & Deliberate

This section walks users through permanent account removal with a strong emphasis on caution and clarity:

#### 🔒 Safety Features:
- **Irreversibility Warning**: A high-visibility alert ensures users know that deletion is permanent and non-recoverable
- **Data Transparency**: Users are informed that all personal data, notes, and progress will be fully erased
- **Confirmation Field**: Requires manual entry of the word "DELETE" in uppercase to prevent accidental deletions

#### ✅ Email Confirmation:
An optional checkbox allows users to receive a final confirmation email after deletion — reinforcing user control and providing a closing audit trail.

#### 📌 UX Considerations:
- The form is centred, focused, and free of clutter to avoid confusion
- Primary actions (like "Delete Account") are clearly marked in red and separated from other navigation to avoid accidental interaction
- Redundant safety warnings offer peace of mind and reinforce accountability

### 👤 Profile Management Access

Beneath the deletion section is a redirect to **Edit Profile**, allowing users to:

- Update their display name and bio
- Maintain full ownership over their identity without needing to access separate forms

This subtle UI cue balances power with accessibility — reminding users that deletion isn't the only form of change available.

### 🔍 Why This Page Matters

While minimalist in design, the Settings Page serves a critical function:

- **🔓 User Autonomy**: Gives users complete control over their data and presence within the app
- **🧠 Intentional Design**: Prevents accidental deletion with strong safeguards and layered confirmations
- **🧼 Clean UX**: Removes friction and mental load from managing account settings — a hallmark of user-respecting platforms

Whether a user is stepping away from the app or just exploring their options, the Settings Page ensures that they feel safe, informed, and in control at all times.

## UX Final Thoughts
The final design of Forge Fitness goes far beyond the initial wireframes and user stories — it delivers a cohesive, accessible, and user-led experience that empowers individuals at every stage of their fitness journey. Each page has been thoughtfully crafted to balance educational content, practical tools, and motivational design — from the intuitive dashboard and expert-guided training section to the reflective lifestyle tracking and goal-setting features. Visual consistency, clear navigation, responsive layouts, and interaction feedback have all been prioritised to ensure users feel confident, motivated, and in control.

Ultimately, the UX of Forge Fitness isn’t just about how the app looks — it’s about how it feels to use: supportive without being overwhelming, structured without being rigid, and personal without sacrificing simplicity. The platform has evolved into a tool that not only guides users through their training, nutrition, and habits but also respects their autonomy and encourages long-term behavioural change. This final design reflects a shift from just using an app to owning a fitness journey — and that’s the experience Forge Fitness was built to deliver.



---

## Database Structure

Forge Fitness employs a modular, relational database structure centered on user authentication, profile personalization, note tracking, and account settings. The schema is designed to be clean, secure, and scalable, providing a practical demonstration of how to structure data for user-driven web applications.

Unlike traditional fitness apps, Forge Fitness does not track live metrics or workouts. Instead, it functions as an educational platform, showcasing how users can manage their fitness journey through structured UI and modular data flow.

![Database](assets/wireframes/database-structure.png)

### 📘 Database Tables

#### 1. users Table
**Purpose**: Stores core user credentials and identity data used for authentication.

**Key Fields**:
- `id` (Primary Key) – Unique user identifier
- `username` (VARCHAR) – Chosen public-facing name
- `email` (VARCHAR) – Used for login
- `password` (TEXT) – Hashed password for security
- `first_name`, `last_name` (VARCHAR) – Optional personal identifiers
- `date_joined` (TIMESTAMP) – When the user registered
- `last_login` (TIMESTAMP) – Most recent login time

🔗 **Related to**: `user_profiles`, `user_settings`, and `notes` tables via foreign keys

#### 2. user_profiles Table
**Purpose**: Separates extended profile content from core login data.

**Key Fields**:
- `user_id` (Foreign Key) – References `users.id`
- `bio` (TEXT) – Custom user-written profile bio
- `profile_picture` (VARCHAR) – Path to uploaded image
- `created_at`, `updated_at` (TIMESTAMP) – Timestamps for record creation and updates

💡 **Why separate?** Enhances modularity and keeps profile content isolated from authentication logic.

#### 3. user_settings Table
**Purpose**: Stores user preferences and account status controls.

**Key Fields**:
- `user_id` (Foreign Key) – References `users.id`
- `account_status` (ENUM: active, deactivated) – Reflects deletion or deactivation
- `theme_preference` (VARCHAR) – Placeholder for future theming options
- `created_at`, `updated_at` (TIMESTAMP) – Tracks lifecycle of settings

🛡️ **Used to drive** the account deletion workflow and allow for future preference toggles.

#### 4. notes Table
**Purpose**: Stores user-generated reflections or logs from various parts of the app.

**Key Fields**:
- `id` (Primary Key) – Unique note ID
- `user_id` (Foreign Key) – References `users.id`
- `title` (VARCHAR) – Note title or heading
- `content` (TEXT) – Body of the note
- `category` (VARCHAR) – Tracks if it's a training, activity, or progression note
- `created_at`, `updated_at` (TIMESTAMP) – Lifecycle tracking

📝 **Enables** multi-category tracking for each user's progress and thoughts.

### 🔄 How It All Works Together

#### ✅ User Authentication & Profile Management
- `users` table handles login, identity, and registration
- `user_profiles` stores profile bios and pictures separately
- Authentication is secure and modular, enabling separation of concerns

#### ⚙️ Account Settings & Deletion
- `user_settings` lets users deactivate their account or store UI preferences
- Ensures user control without complex relational overhead

#### 🗂️ Notes & Progress Tracking
- `notes` table powers all logging, journaling, and reflection
- Categorised notes are easily filtered and maintained across the UI 

### **Scalability & Future Enhancements**  

While Forge Fitness currently maintains **a lightweight database structure**, it is **designed for easy expansion** if additional features (e.g., **theme preferences, notification settings**) are needed in the future.  

By keeping the database **minimal and efficient**, Forge Fitness remains **focused on UI demonstration** rather than **complex data storage**.

---

## Folder Structure

The Forge Fitness project follows a modular and structured approach to maintain scalability, clarity, and maintainability. This refactored structure ensures that user authentication, profile management, and settings are well-organized while keeping the core Django project structure intact.

### 🔹 How It’s Organized  

✔ **User authentication & profile management** are handled in the `users/` directory.  
✔ **User settings & account preferences** are managed in the `settings/` directory.  
✔ **Core Django settings, static assets, and templates** are stored in the `forge_fitness/` directory.  
✔ **Project-wide assets**, including wireframes and diagrams, are contained in the `assets/` directory.  


![Folder Structure](assets/wireframes/folder_structure.png)

### How It Works

Each directory corresponds to a specific feature or functionality of the application:

1. **Root Directory (`forge-fitness/`)**  
   - Contains project-wide configurations such as:  
     - `manage.py` – Django project management script.  
     - `requirements.txt` – Dependencies and package requirements.  
     - `.env` – Environment variables for database credentials and secrets.  

2. **Main Application (`forge_fitness/`)**  
   - Manages the core Django project settings, including:  
     - `settings.py` – Configuration for installed apps, middleware, database settings.  
     - `urls.py` – Central URL routing for the project.  
     - `wsgi.py` & `asgi.py` – Deployment configurations.  
   - Contains **static files (`static/`)** used across the entire project.  
   - Stores **global templates (`templates/`)**, including:  
     - `base.html` – Layout foundation for all pages.  
     - `navbar.html` – Shared navigation bar.  
     - `footer.html` – Common footer section.  

3. **User Module (`users/`)**  
   - Handles **user authentication and profile management**.  
   - Contains:  
     - `models.py` – User database schema (storing login credentials, profile details).  
     - `views.py` – Handles authentication workflows (signup, login, profile updates).  
     - `forms.py` – Form handling for user authentication.  
   - Templates include:  
     - `signup.html` – User registration page.  
     - `login.html` – Login interface.  
     - `profile.html` – User profile settings.  

4. **Settings Module (`settings/`)**  
   - Manages **user account preferences and status settings**.  
   - Contains:  
     - `models.py` – Stores user preferences (e.g., account status).  
     - `views.py` – Manages user settings adjustments.  
     - `urls.py` – Routing for settings-related actions.  
   - Templates include:  
     - `preferences.html` – UI for modifying user settings.  
     - `notifications.html` – Page for adjusting notification preferences.  

5. **Assets & Wireframes (`assets/`)**  
   - Stores project documentation and design references, including:  
     - `wireframes/` – Screenshots of UI wireframes.  
     - `diagrams/` – Visual representations of the database and folder structure.  

---

### 🔹 How It Ties Into the Database  

The **folder structure** directly reflects the **database schema**, ensuring a **one-to-one mapping between functionalities and data storage**:

- The **`users/` app** aligns with the **User Table**, managing authentication and profile data.  
- The **`settings/` app** links to the **Settings Table**, handling user preferences.  

By **maintaining this structured relationship**, the project ensures a **seamless flow of data** between the backend and frontend, making it easier to **scale and manage future enhancements**.  

---

## Technologies Used

Forge Fitness is built using a comprehensive modern web development stack that prioritizes security, scalability, and user experience. The application leverages Django's robust framework capabilities combined with responsive frontend technologies to deliver a seamless fitness management platform. The technology choices reflect industry best practices for full-stack development, ensuring maintainable code, secure user authentication, and optimal performance across devices.

### Backend Framework & Core Technologies

| Technology | Description |
|------------|-------------|
| **Python 3.8+** | Primary programming language powering the application |
| **Django 4.2+** | Full-stack web framework used for rapid development, including authentication, ORM, forms, admin, security, and modular app structure |
| **Django Authentication System** | User authentication flows with a custom backend for email or username login (`users/backends.py`) |
| **Django ORM & Migrations** | Robust object-relational mapping, database migrations, and model relationships (ForeignKey, OneToOne) |
| **Django Forms & Messages** | Secure form handling, server-side validation, and user feedback notifications |
| **Django Admin Interface** | Administrative dashboard for managing users and data |
| **SQLite (Dev) / PostgreSQL (Production)** | Lightweight development database; scalable PostgreSQL support for deployment |
| **WSGI / ASGI** | Production-ready server interfaces (`wsgi.py`, `asgi.py`) for deployment flexibility |

### Frontend Technologies & Libraries

| Technology | Description |
|------------|-------------|
| **HTML5 & CSS3** | Semantic markup and custom CSS for site structure and branding |
| **Bootstrap 5** | Responsive grid, UI components, and utilities for a mobile-first design |
| **JavaScript (ES6+) & jQuery** | Client-side interactivity, AJAX requests, and dynamic DOM updates |
| **Chart.js** | Data visualization—renders interactive bar, line, and pie charts on the dashboard |
| **Django Template Language** | Server-rendered templates with template inheritance, custom tags, and filters |

### Security & Authentication

| Technology | Description |
|------------|-------------|
| **Custom Authentication Backend** | Secure email/username login (see `users/backends.py`) |
| **Custom Middleware** | Request/response processing, user session management (`users/middleware.py`) |
| **Django Security Middleware** | Built-in protections: CSRF, XSS, secure headers, password hashing |
| **Form & File Upload Validation** | Strict server-side input checks, image file validation for profile pictures and uploads |

### Database & Data Models

| Technology | Description |
|------------|-------------|
| **Django Models** | Modular models for user profiles, practice notes, personal settings, and activity logs |
| **Django Migrations** | Schema management and version control |
| **Relational Data Design** | ForeignKey and OneToOne relationships for scalable data organization |

### Application Architecture & Design Patterns

| Technology | Description |
|------------|-------------|
| **Class-Based Views (CBVs)** | Clean, reusable views for efficient logic separation |
| **Django Apps Architecture** | Modular, scalable app design for maintainability |
| **Template Inheritance** | DRY (Don't Repeat Yourself) UI with shared base templates |
| **RESTful URL Routing** | Intuitive and consistent navigation |

### Development Tools & Utilities

| Technology | Description |
|------------|-------------|
| **Virtual Environment** | Dependency isolation and environment management |
| **WhiteNoise** | Efficient static file serving in production environments |
| **Environment Variables** | Secure configuration for sensitive deployment settings |
| **Procfile & runtime.txt** | Explicit deployment configuration for Render (or Heroku compatibility) |
| **Static & Media File Management** | Separation of static assets and user-uploaded media |
| **Python Logging** | Application error tracking and debugging |

### Features & User Experience

| Technology | Description |
|------------|-------------|
| **User Registration & Login** | Custom signup/authentication, including form validation and messaging |
| **Profile Management** | Customizable user profiles with avatar upload and bio |
| **Practice Notes System** | Full CRUD operations for user-created notes (create, view, edit, delete) |
| **Dashboard Analytics** | Real-time progress tracking, statistics, and interactive charts |
| **Account Settings** | Editable preferences, password management, and account deletion |
| **Custom Error Pages** | User-friendly 404 and 500 error handling |
| **Responsive, Mobile-First Design** | Seamless experience across devices |
| **AJAX Integration** | Asynchronous chart and content updates without page reloads |
| **File Upload Handling** | Secure image validation and storage |

---

This comprehensive technology stack demonstrates proficiency in modern full-stack development practices while ensuring Forge Fitness delivers a secure, scalable, and user-friendly fitness management platform. The combination of Django's robust backend capabilities with responsive frontend technologies creates an application that meets professional development standards and provides an exceptional user experience across all devices and use cases.

---

## Security Features

Forge Fitness implements a comprehensive security framework that follows Django best practices and industry standards to protect user data, prevent common web vulnerabilities, and ensure secure authentication flows. The application employs multiple layers of security controls, from secure password handling and input validation to protection against common attack vectors like CSRF, XSS, and SQL injection.

### Authentication & Authorization

| Security Feature | Implementation |
|------------------|----------------|
| **Custom Authentication Backend** | Implements a custom backend (`users/backends.py`) allowing secure login via email or username, ensuring authentication logic is isolated and protected from common exploits |
| **Password Hashing & Storage** | User passwords are never stored in plain text. Django's default PBKDF2 password hasher is used to securely hash and salt all passwords |
| **User Authorization & Access Control** | Views and templates are protected using Django's built-in `@login_required` decorators and permission checks, so users cannot access or modify data they don't own |
| **Session Management** | Custom middleware (`users/middleware.py`) ensures that user sessions and sensitive operations are handled securely |

### Input Validation & Data Protection

| Security Feature | Implementation |
|------------------|----------------|
| **Form Validation & Sanitization** | All user inputs—across signup, login, note creation, and profile editing—are validated server-side to prevent injection attacks and invalid data from entering the database |
| **File Upload Validation** | Strict checks on image uploads (type, size) for avatars/profile pictures to block malicious files and prevent abuse |
| **SQL Injection Protection** | Django ORM provides automatic protection against SQL injection attacks through parameterized queries |
| **XSS Prevention** | Django's template system automatically escapes user input, and form validation prevents malicious script injection |

### Web Security & Headers

| Security Feature | Implementation |
|------------------|----------------|
| **Django Security Middleware** | Leverages Django's built-in middleware for automatic CSRF (Cross-Site Request Forgery) protection, XSS (Cross-Site Scripting) prevention, secure HTTP headers, and session security |
| **Secure Cookie Settings** | Uses Django's recommended cookie settings for session cookies (HTTPOnly, Secure, SameSite) to protect user authentication tokens from interception or cross-site attacks |
| **HTTPS Deployment Ready** | The application is ready for deployment behind HTTPS (recommended by both Django and Render), securing all data in transit |
| **Secure Headers** | Implements security headers including X-Frame-Options, X-Content-Type-Options, and X-XSS-Protection |

### Configuration & Environment Security

| Security Feature | Implementation |
|------------------|----------------|
| **Environment Variables for Secrets** | Sensitive settings (like secret keys and database credentials) are managed via environment variables, never hard-coded or exposed in the repository |
| **Error Handling & Information Disclosure** | Custom 404 and 500 pages prevent leakage of sensitive information, and debug settings are disabled in production |
| **Production Configuration** | Debug mode is disabled in production, and sensitive configuration is properly secured |

### Additional Security Considerations

While Forge Fitness implements robust security measures, the following enhancements could be considered for future development:

- **Rate Limiting**: Implement request throttling to prevent brute force attacks
- **Content Security Policy (CSP)**: Add CSP headers to prevent code injection attacks
- **Security Logging**: Enhanced logging for security events and failed authentication attempts
- **Two-Factor Authentication (2FA)**: Optional secondary authentication for enhanced account security
- **Password Strength Requirements**: Enforce stronger password policies during registration

The security implementation in Forge Fitness demonstrates a comprehensive understanding of web application security principles and provides a solid foundation for protecting user data and maintaining application integrity in production environments.

---

## Testing

Forge Fitness has undergone comprehensive testing to ensure functionality, security, and user experience across all features and devices. Testing includes automated unit tests, manual functionality testing, responsive design validation, and security verification.

**📋 For detailed testing documentation, including test cases, validation results, and bug fixes, please refer to:**

**[Testing Documentation](testing/test.md)**

This dedicated testing file contains:
- Manual testing procedures and results
- Automated test coverage reports
- User acceptance testing scenarios
- Cross-browser and device compatibility testing
- Security and performance validation
- Known issues and resolutions

All critical user journeys, authentication flows, CRUD operations, and security features have been thoroughly tested and validated before deployment.

---

## Future Enhancements

Forge Fitness has been designed with scalability and user experience expansion in mind. The following enhancements represent realistic and valuable additions that would further improve the educational and organizational aspects of the platform while maintaining its core mission of fitness guidance and personal development.

### User Experience & Accessibility

| Enhancement | Description | Impact |
|-------------|-------------|---------|
| **Dark Mode & Accessibility Improvements** | Implement a dark mode toggle and enhanced accessibility options (font size, color contrast, ARIA labels) to improve usability for all users | Improved accessibility compliance and user comfort during extended use |
| **Multi-Language Support** | Internationalize the app by supporting multiple languages, making it accessible to a wider audience | Expanded global reach and inclusivity |
| **Enhanced Chart Customization** | Allow users to customize dashboard charts—selecting timeframes, toggling data categories, or switching chart types for a more personalized analytics view | Increased user engagement with progress visualization |

### Data Management & Export

| Enhancement | Description | Impact |
|-------------|-------------|---------|
| **User Progress Export (PDF/CSV)** | Allow users to export their activity statistics, notes, or progress charts as PDF or CSV files for offline tracking, printing, or sharing with coaches | Enhanced data portability and professional sharing capabilities |
| **Bulk Note Management** | Add multi-select or bulk-delete options for users to more easily manage their practice notes | Improved efficiency for active users with extensive note histories |

### Communication & Engagement

| Enhancement | Description | Impact |
|-------------|-------------|---------|
| **Email Notifications & Reminders** | Add automated email reminders for users to log notes, reflect on progress, or receive encouragement based on inactivity or milestones | Increased user retention and consistent platform engagement |
| **In-App Announcements or Tips** | Admins can post platform updates, health tips, or feature guides to a news feed or announcement banner on the dashboard | Enhanced user education and platform communication |

### Privacy & Administration

| Enhancement | Description | Impact |
|-------------|-------------|---------|
| **Profile Privacy Settings** | Enable users to set their profile as public/private and control what profile information or progress data is visible to others (if you ever introduce a social or community feature) | Enhanced user privacy control and foundation for potential social features |
| **Admin Analytics Dashboard** | Build an admin-only analytics panel to track overall user activity, signups, and platform engagement (good for growth and maintenance) | Improved platform management and data-driven decision making |

---

Each enhancement maintains the platform's focus on education and personal development while adding meaningful value to the user experience without compromising the clean, intuitive design that defines Forge Fitness.

---

## Local Development Setup

Follow these step-by-step instructions to set up Forge Fitness for local development on your machine.

### Prerequisites

Ensure you have the following installed on your system:

| Requirement | Version | Purpose |
|-------------|---------|---------|
| **Python** | 3.8+ | Core programming language |
| **pip** | Latest | Package manager for Python |
| **Git** | Latest | Version control system |
| **Virtual Environment** | `venv` or `virtualenv` | Dependency isolation |

### Step-by-Step Setup

#### 1. Clone the Repository

```bash
git clone https://github.com/GBerrow/Forge-Fitness.git
cd Forge-Fitness
```

#### 2. Create and Activate Virtual Environment

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

#### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

#### 4. Environment Variables Setup

Create a `.env` file in the project root directory:

```bash
# Create .env file
touch .env
```

Add the following environment variables to your `.env` file:

```env
# Django Settings
SECRET_KEY=your-secret-key-here
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1

# Database (SQLite for development)
DATABASE_URL=sqlite:///db.sqlite3

# Optional: Email Configuration (for future features)
EMAIL_BACKEND=django.core.mail.backends.console.EmailBackend
```

**⚠️ Important**: Never commit your `.env` file to version control. It's already included in `.gitignore`.

#### 5. Database Setup

Run Django migrations to create the database schema:

```bash
python manage.py makemigrations
python manage.py migrate
```

#### 6. Create Superuser Account

Create an admin account for accessing the Django admin interface:

```bash
python manage.py createsuperuser
```

Follow the prompts to set up your admin credentials.

#### 7. Collect Static Files

```bash
python manage.py collectstatic
```

#### 8. Run the Development Server

```bash
python manage.py runserver
```

The application will be available at: **http://127.0.0.1:8000/**

### Accessing the Application

| URL | Purpose | Access |
|-----|---------|---------|
| `http://127.0.0.1:8000/` | Main application | Public |
| `http://127.0.0.1:8000/admin/` | Django admin interface | Superuser only |
| `http://127.0.0.1:8000/signup/` | User registration | Public |
| `http://127.0.0.1:8000/login/` | User login | Public |

### Development Workflow

#### Making Changes

1. **Code Changes**: Edit files in your preferred IDE
2. **Database Changes**: Create and run migrations
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```
3. **Static Files**: Collect static files after CSS/JS changes
   ```bash
   python manage.py collectstatic
   ```

#### Running Tests

```bash
python manage.py test
```

#### Checking for Issues

```bash
python manage.py check
```

### Common Troubleshooting

| Issue | Solution |
|-------|----------|
| **Module not found errors** | Ensure virtual environment is activated and dependencies are installed |
| **Database errors** | Run `python manage.py migrate` to update database schema |
| **Static files not loading** | Run `python manage.py collectstatic` and check `STATIC_URL` settings |
| **Port already in use** | Use a different port: `python manage.py runserver 8001` |
| **Permission denied** | Check file permissions and virtual environment activation |

### Development Tips

- **Virtual Environment**: Always ensure your virtual environment is activated before running commands
- **Database Reset**: To start fresh, delete `db.sqlite3` and run migrations again
- **Admin Access**: Use the superuser account to manage users and data through the admin interface
- **Debug Mode**: Keep `DEBUG=True` in development for detailed error messages
- **Hot Reload**: The development server automatically reloads when you make code changes

### Project Structure

```
Forge-Fitness/
├── forge_fitness/          # Main Django project
├── users/                  # User authentication app
├── static/                 # Static files (CSS, JS, images)
├── templates/              # HTML templates
├── assets/                 # Documentation and wireframes
├── manage.py              # Django management script
├── requirements.txt       # Python dependencies
├── .env                   # Environment variables (create this)
└── README.md             # This file
```

Once setup is complete, you'll have a fully functional local development environment ready for contributing to Forge Fitness!

---

## Deployment

Forge Fitness is configured for seamless deployment to modern cloud platforms, with Render being the recommended hosting solution. The application uses PostgreSQL for production database management and WhiteNoise for efficient static file serving.

### Production Requirements

| Requirement | Purpose | Configuration |
|-------------|---------|---------------|
| **PostgreSQL Database** | Production-grade database | Managed database service |
| **Python Runtime** | Application execution | Python 3.8+ |
| **WhiteNoise** | Static file serving | Configured in `settings.py` |
| **Gunicorn** | WSGI HTTP Server | Production web server |
| **Environment Variables** | Secure configuration | Platform-specific settings |

### Pre-Deployment Checklist

Before deploying, ensure the following configurations are in place:

#### ✅ Production Settings

- [ ] `DEBUG = False` in production environment
- [ ] `ALLOWED_HOSTS` configured with your domain
- [ ] Database URL configured for PostgreSQL
- [ ] Static files configuration verified
- [ ] Security middleware enabled
- [ ] Environment variables properly set

#### ✅ Required Files

- [ ] `requirements.txt` - Python dependencies
- [ ] `runtime.txt` - Python version specification
- [ ] `Procfile` - Process configuration
- [ ] Environment variables configured

### Deployment to Render

#### Step 1: Prepare Repository

Ensure your repository contains these deployment files:

**runtime.txt:**
```
python-3.9.18
```

**Procfile:**
```
web: gunicorn forge_fitness.wsgi:application
```

**requirements.txt** (verify these key dependencies are included):
```
Django>=4.2.0
psycopg2-binary>=2.9.0
whitenoise>=6.5.0
gunicorn>=21.2.0
```

#### Step 2: Create Render Web Service

1. **Connect Repository**
   - Log in to [Render](https://render.com/)
   - Click "New +" → "Web Service"
   - Connect your GitHub repository

2. **Configure Build Settings**
   
   | Setting | Value |
   |---------|-------|
   | **Name** | `forge-fitness` |
   | **Environment** | `Python 3` |
   | **Build Command** | `pip install -r requirements.txt` |
   | **Start Command** | `gunicorn forge_fitness.wsgi:application` |

#### Step 3: Database Configuration

1. **Create PostgreSQL Database**
   - In Render dashboard: "New +" → "PostgreSQL"
   - Choose your preferred plan
   - Note the connection details

2. **Configure Database Environment Variables**

#### Step 4: Environment Variables

Configure the following environment variables in Render:

| Variable | Value | Purpose |
|----------|-------|---------|
| `SECRET_KEY` | `your-production-secret-key` | Django security |
| `DEBUG` | `False` | Production mode |
| `DATABASE_URL` | `postgresql://user:pass@host:port/db` | Database connection |
| `ALLOWED_HOSTS` | `your-app-name.onrender.com` | Allowed domains |

**⚠️ Important**: Generate a new `SECRET_KEY` for production. Never use your development key.

#### Step 5: Static Files Configuration

Ensure `settings.py` includes:

```python
# Static files configuration
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# WhiteNoise middleware
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    # ... other middleware
]
```

#### Step 6: Deploy Application

1. **Push to Repository**
   ```bash
   git add .
   git commit -m "Deploy to production"
   git push origin main
   ```

2. **Render Auto-Deploy**
   - Render will automatically detect changes
   - Monitor build logs for any issues
   - Deployment typically takes 2-5 minutes

### Post-Deployment Setup

#### Database Migrations

After successful deployment, run migrations:

1. **Access Render Shell**
   - Go to your web service dashboard
   - Click "Shell" tab
   - Run migration commands

2. **Execute Migrations**
   ```bash
   python manage.py migrate
   ```

3. **Create Superuser** (Optional)
   ```bash
   python manage.py createsuperuser
   ```

#### Verify Deployment

| Check | URL | Expected Result |
|-------|-----|-----------------|
| **Homepage** | `https://your-app.onrender.com/` | Welcome page loads |
| **Static Files** | Check CSS/JS loading | Styles applied correctly |
| **Authentication** | `/signup/` and `/login/` | Forms work properly |
| **Database** | User registration | Data saves successfully |
| **Admin Panel** | `/admin/` | Admin interface accessible |

### Production Monitoring

#### Health Checks

Monitor these key metrics:

- **Application Status**: Service running without errors
- **Database Connectivity**: Successful database connections
- **Static Files**: CSS/JS loading properly
- **User Authentication**: Login/signup functionality
- **Error Rates**: Monitor for 500/404 errors

#### Log Monitoring

Access logs through:
- **Render Dashboard**: Service logs tab
- **Django Admin**: For application-level monitoring
- **Database Logs**: PostgreSQL query performance

### Common Deployment Issues

| Issue | Cause | Solution |
|-------|-------|----------|
| **Build Failed** | Missing dependencies | Check `requirements.txt` |
| **Database Connection Error** | Incorrect DATABASE_URL | Verify PostgreSQL connection string |
| **Static Files Not Loading** | WhiteNoise misconfiguration | Check `STATIC_ROOT` and middleware |
| **500 Internal Server Error** | `DEBUG=True` in production | Set `DEBUG=False` |
| **ALLOWED_HOSTS Error** | Missing domain | Add your Render domain to `ALLOWED_HOSTS` |

### Security Considerations

#### Production Security Settings

Ensure these settings are configured for production:

```python
# Security settings
SECURE_SSL_REDIRECT = True
SECURE_HSTS_SECONDS = 3600
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_BROWSER_XSS_FILTER = True
```

#### Environment Variables Security

- **Never commit secrets** to version control
- **Use strong SECRET_KEY** (50+ characters)
- **Rotate credentials** regularly
- **Monitor access logs** for suspicious activity

### Maintenance & Updates

#### Regular Updates

1. **Dependencies**: Keep packages updated
2. **Security Patches**: Apply Django security updates
3. **Database Maintenance**: Monitor performance
4. **Backup Strategy**: Regular database backups

#### Deployment Workflow

```bash
# 1. Test locally
python manage.py test

# 2. Update dependencies
pip freeze > requirements.txt

# 3. Deploy to production
git add .
git commit -m "Update: [description]"
git push origin main
```

After following these instructions you will have a production-ready application ! 🚀

---

## Credits

The development of Forge Fitness represents both individual effort and the collective contributions of the broader fitness education and web development communities. This project demonstrates comprehensive full-stack development skills while creating a meaningful platform that empowers users to take control of their fitness journey through education, organization, and personal development.

### Core Development

| Contribution Area | Details |
|-------------------|---------|
| **Primary Development** | • Fully designed and implemented by myself<br>• Complete Django application architecture and implementation<br>• User authentication, profile management, and note-taking systems<br>• Educational content organization and user experience design<br>• Testing, security implementation, and performance optimization |
| **Architecture & Design** | • Original modular Django application structure with separation of concerns<br>• User-centered design with responsive interface implementation<br>• Educational content framework with interactive note-taking capabilities<br>• Database schema design with secure user data management<br>• RESTful URL routing and template inheritance patterns |
| **Technical Implementation** | • Custom authentication backend supporting email/username login<br>• Comprehensive form validation and security middleware integration<br>• Interactive dashboard with Chart.js data visualization<br>• Cross-browser compatibility and mobile-first responsive design<br>• Production deployment with PostgreSQL and static file optimization |

### External Resources & Tools

#### Fitness Education & Content

| Resource | Contribution to Project |
|----------|-------------------------|
| **Jeff Nippard** | • Science-based fitness education and training methodology<br>• YouTube content integration for structured workout guidance<br>• Exercise demonstration videos for all major muscle groups<br>• Evidence-based training principles and progressive overload concepts<br>• Educational approach to fitness that prioritizes form and safety |
| **Jeff Nippard's YouTube Channel** | • Curated video content for muscle-specific training sections<br>• Expert-led exercise demonstrations and technique instruction<br>• Training plan development and periodization guidance<br>• Nutrition and recovery education supporting holistic fitness |
| **Fitness Industry Research** | • Market analysis data supporting feature development decisions<br>• User behavior statistics informing UX design and engagement strategies<br>• Retention and motivation research guiding achievement systems<br>• Mobile-first design statistics supporting responsive development |

#### Web Development Framework & Libraries

| Technology | Contribution to Project |
|------------|-------------------------|
| **Django 4.2+** | • Full-stack web framework providing robust foundation<br>• Built-in authentication system with custom backend integration<br>• ORM for database management and migrations<br>• Admin interface for content and user management<br>• Security middleware and CSRF protection |
| **Bootstrap 5** | • Responsive CSS framework for mobile-first design<br>• UI components and utilities for consistent styling<br>• Grid system supporting cross-device compatibility<br>• Form styling and validation feedback integration |
| **Chart.js** | • Interactive data visualization library for dashboard analytics<br>• Responsive chart rendering for progress tracking<br>• Multiple chart types (bar, line, pie) for diverse data representation<br>• Customizable styling matching application branding |
| **jQuery** | • JavaScript library for DOM manipulation and AJAX functionality<br>• Enhanced user interactions and dynamic content updates<br>• Form handling and validation feedback<br>• Smooth UI transitions and user experience enhancements |

#### Development & Deployment Tools

| Tool/Platform | Application in Project |
|---------------|------------------------|
| **GitHub** | • Version control and repository hosting throughout development<br>• Issue tracking and project management<br>• Collaboration platform for code review and documentation<br>• Integration with deployment pipeline |
| **Render** | • Cloud hosting platform for production deployment<br>• Managed PostgreSQL database hosting<br>• Automatic deployments from GitHub repository<br>• SSL certificate management and domain configuration |
| **Visual Studio Code** | • Primary development environment with Django extensions<br>• Integrated terminal for Django management commands<br>• Git integration for version control workflow<br>• Syntax highlighting and code completion for Python/Django |
| **PostgreSQL** | • Production database providing scalable data storage<br>• Robust relational database for user profiles and notes<br>• Advanced query capabilities for data analytics<br>• Reliable backup and recovery systems |
| **ChatGPT**  |• AI-powered coding assistant for debugging and code suggestions<br>• Code review and optimization recommendations<br>• Learning resource for Django best practices |


#### Design & User Experience Resources

| Resource | Contribution to Project |
|----------|-------------------------|
| **Color Palette Development** | • Brand color scheme research and implementation<br>• Accessibility-compliant color contrast ratios<br>• Psychological color theory application for motivation<br>• Consistent visual identity across all interface elements |
| **Bootstrap Icons** | • Comprehensive icon library for UI elements<br>• Scalable vector icons for responsive design<br>• Semantic iconography supporting user understanding<br>• Consistent visual language throughout application |
| **Wireframing & Planning** | • Initial design conceptualization and user flow mapping<br>• Responsive layout planning across device sizes<br>• User journey optimization and navigation structure<br>• Feature prioritization based on user needs analysis |

### Technical Acknowledgments

| Organization/Community | Contribution |
|------------------------|-------------|
| **Django Software Foundation** | • Development and maintenance of the exceptional Django framework<br>• Comprehensive documentation and tutorials enabling rapid development<br>• Security-focused approach with built-in protections<br>• Active community support and continuous framework improvements |
| **Python Software Foundation** | • Python language development and maintenance<br>• Extensive standard library supporting web development<br>• Package Index (PyPI) ecosystem enabling third-party integrations<br>• Documentation and learning resources for language mastery |
| **Web Development Community** | • Modern web development patterns and best practices<br>• Accessibility standards implementation guidance<br>• Performance optimization techniques for web applications<br>• Security best practices for user data protection |
| **Open Source Community** | • WhiteNoise for static file serving in production<br>• Gunicorn for production WSGI server implementation<br>• Psycopg2 for PostgreSQL database connectivity<br>• Countless other libraries enabling rapid development |

### Special Thanks

| Recipient | Contribution to Project |
|-----------|-------------------------|
| **Code Institute** | • Comprehensive full-stack development curriculum providing foundational knowledge<br>• Project assessment framework encouraging industry-standard implementation<br>• Django specialization course covering advanced web development concepts<br>• Community of peers offering feedback and collaborative learning |
| **Project Mentor** | • Architectural guidance ensuring scalable, maintainable code structure<br>• Code review and optimization recommendations<br>• Best practice advice for Django development and deployment<br>• Testing strategy guidance and quality assurance principles |
| **Jeff Nippard** | • Exceptional educational content that forms the foundation of training guidance<br>• Evidence-based approach to fitness education<br>• Permission and inspiration for integrating science-based training content<br>• Commitment to accessible, high-quality fitness education |
| **Fitness Education Community** | • Research and insights into effective fitness motivation and habit formation<br>• User experience patterns from successful fitness applications<br>• Educational content strategies for skill development and retention<br>• Holistic approach to health and wellness beyond just exercise |
| **Testing Participants** | • Valuable feedback during development iterations and user testing<br>• Bug reporting and edge case identification across devices<br>• Usability insights from various technical skill levels<br>• Performance feedback across diverse devices and browsers |

### Copyright & Educational Use

This project has been developed for educational purposes as part of a portfolio demonstration showcasing full-stack web development capabilities. All external resources, libraries, and educational content have been used in accordance with their respective licenses and terms of use.

- Educational content references and workout guidance are properly attributed to their original creators
- All code represents original work built upon open-source frameworks and libraries
- No proprietary fitness content or copyrighted material has been used without permission
- Fair use principles have been applied to all referenced materials

### Legacy & Future Development

This project stands on the shoulders of those who have advanced web development, fitness education, and user experience design, combining these disciplines to create an accessible yet comprehensive fitness management platform. The foundation laid by these contributors enables future enhancements and continued evolution of the platform.


---

**This project represents a synthesis of technical expertise, educational content, and user-centered design, made possible through the collective contributions of the communities and individuals acknowledged above.** 🙏

---

### Just to save yourself scrolling back to the top:

- [Introduction](#introduction)
- [Target Audience & User Needs](#target-audience--user-needs)
  - [Beginners & First-Time Gym-Goers](#beginners--first-time-gym-goers)
  - [Intermediate Users & Returning Lifters](#intermediate-users--returning-lifters)
  - [Advanced Gym-Goers](#advanced-gym-goers)
  - [Digital-First & Time-Conscious Users](#digital-first--time-conscious-users)
  - [Progress-Focused & Analytical Users](#progress-focused--analytical-users)
- [Client Goals](#client-goals)
- [User Stories](#user-stories)
- [Statistics](#statistics)
- [Initial Design](#initial-design)
  - [Colour Scheme](#colour-scheme)
  - [Typography](#typography)
- [Wireframes](#wireframes)
   - [Sign up Page](#sign-up-page)
   - [Login Page](#login-page)
   - [Home Page](#home-page)
   - [Workout Page](#workout-page)
   - [Progress Page](#progress-page)
   - [Profile Page](#profile-page)
   - [Settings Page](#settings-page)
- [User Experience | Final Design](#user-experience--final-design)
  - [Dashboard Overview](#dashboard-overview)
  - [Sign Up Page | Final Design](#sign-up-page--final-design)
  - [Login Page | Final Design](#login-page--final-design)
  - [Training Page | Final Design](#training-page--final-design)
  - [Activity Page | Final Design](#activity-page--final-design)
  - [Progression Page | Final Design](#progression-page--final-design)
  - [Settings Page | Final Design](#settings-page--final-design)
  - [Final Thoughts](#final-thoughts)
- [Database Structure](#database-structure)
- [Folder Structure](#folder-structure)
- [Technologies Used](#technologies-used)
- [Security Features](#security-features)
- [Testing](#testing)
- [Future Enhancements](#future-enhancements)
- [Local Development Setup](#local-development-setup)
- [Deployment](#deployment)
- [Credits](#credits)

**Test documentation on this link** [👉 Click Here!](./testing/test.md)

---