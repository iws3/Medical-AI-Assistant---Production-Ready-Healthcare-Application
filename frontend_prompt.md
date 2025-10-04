prompt 1->"DOCUMENTATION"

Given this API service already hosted on Render, please write comprehensive API documentation that explains the flow of the application. The documentation should clearly describe the available endpoints, their request/response structures, and include example responses. The purpose is to guide frontend developers so they can build a fully functional frontend for this application.

Do not provide frontend code; instead, focus only on minimal but clear guidance about how each endpoint is structured and how the responses should be interpreted.

Render URL: https://medical-ai-assistant-production-ready.onrender.com/



prompt 2-> FRONTEND DEVELOPMENT


Build a single-page Next.js 15 app using App Router, TypeScript, and Tailwind CSS with a medical blue-orange-white color palette: Primary blue `#2563eb` (blue-600), Secondary orange `#f97316` (orange-500), Accent `#1e40af` (blue-800), Background white `#ffffff`, Light gray `#f1f5f9` (slate-100). 

Create a tabs-based interface with four sections: (1) Welcome Tab as default showing hero section with app features, medical disclaimer, and "Get Started" CTA with gradient background;

 (2) Chat Tab with message bubbles (user messages in orange, AI in blue), input field at bottom, and suggested question chips above input like "Symptoms of malaria?", "What causes headaches?", "Diabetes management tips";

 (3) Analysis Tab offering two input methods - drag-and-drop file upload zone OR camera capture button, displaying extracted text in a card first, then showing structured analysis with Summary, Key Findings , Recommendations , and Next Steps  sections in expandable cards; 

(4) Research Tab with search bar, medical topic suggestion chips like "Diabetes guidelines", "Hypertension treatment", "Malaria prevention", displaying results as cards with source badges (PubMed, WHO, CDC) and AI-generated summary highlighted at top. 


Add a fixed bottom-right floating button to toggle language between English (🇬🇧 flag emoji) and French (🇫🇷 flag emoji) that persists across all tabs. Include loading skeletons for API calls, toast notifications for errors, copy-to-clipboard buttons on results, smooth tab transitions with underline indicators, and prominent medical disclaimer 


"⚠️ For informational purposes only - Always consult healthcare professionals" on every tab. Use API base URL `https://medical-ai-assistant-production-ready.onrender.com` with endpoints from documentation. Ensure responsive mobile-first design with professional medical UI, trust indicators, and accessible form controls.