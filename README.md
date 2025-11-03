#️⃣ EU AI Act RAG Asistanı
Bu proje, Avrupa Birliği Yapay Zeka Yasası (EU AI Act) hakkında soruları yanıtlamak için Retrieval-Augmented Generation (RAG) mimarisini kullanan bir sohbet asistanıdır. Asistan, yalnızca resmi AB kaynaklarını kullanarak yüksek doğrulukta ve bağlama dayalı yanıtlar üretir.
✨ Temel ÖzelliklerUzman Bilgi Tabanı: 
EU AI Act'in resmi metinleri ve SSS sayfaları bilgi kaynağı olarak kullanılır.Stateful RAG: Sohbet geçmişini hatırlar ve takip eden soruları bağlamına uygun şekilde yanıtlar.Modern LangChain: LangChain Expression Language (LCEL) kullanılarak modüler ve okunabilir zincirler oluşturulmuştur.WSL & UV Optimizasyonu: Linux (WSL) ortamında hızlı ve hafif uv paket yöneticisi ile bağımlılıklar yönetilir.
🛠️ Teknoloji YığınıBileşenTeknolojiAmaçPaket YöneticisiuvHızlı bağımlılık yönetimi.Geliştirme OrtamıVSCode & WSL (Ubuntu/Debian)Linux üzerinde sorunsuz geliştirme.LLM & EmbeddingsGoogle Gemini (Gemini-2.5-Flash, text-embedding-004)Yapay zeka modeli ve metin gömülmeleri.Vektör VeritabanıChromaDBBelgeleri depolama ve hızlı sorgulama.ÇerçeveLangChainRAG zincirlerini oluşturma ve yönetme.
🌐 Bilgi Kaynakları (Knowledge Base)Uygulama, aşağıda belirtilen tam olarak bu resmi AB kaynaklarını tarayarak güncel bilgi tabanını oluşturur:
https://eur-lex.europa.eu/eli/reg/2024/1689/oj/enghttps://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-aihttps://commission.europa.eu/news-and-media/news/ai-act-enters-force-2024-08-01_enhttps://digital-strategy.ec.europa.eu/en/faqs/general-purpose-ai-models-ai-act-questions-answers
⚙️ Kurulum ve Çalıştırma
Bu projenin WSL (Windows Subsystem for Linux) ortamında çalıştırılması önerilir.
1. Ön KoşullarPython 3.10+uv (Pipx aracılığıyla kurulabilir: pipx install uv)GOOGLE_API_KEY (Google AI Studio'dan alınmış bir anahtar)2. Proje KurulumuBash# 1. Depoyu klonla (WSL terminalinde)
git clone https://github.com/KULLANICI_ADINIZ/AI_Act_RAG.git
cd AI_Act_RAG

# 2. Ortam değişkenini ayarla
echo "GOOGLE_API_KEY=AIzaSy************************" > .env

# 3. Bağımlılıkları kur
# (uv, gereksinimleri çok hızlı bir şekilde kuracaktır)
uv sync

# NOT: ingest.py dosyasındaki pysqlite3 entegrasyonu, ChromaDB'nin WSL'de sorunsuz çalışmasını sağlar.
3. Veri Yükleme (Ingestion)İlk çalıştırmada, web kaynakları taranır, parçalara ayrılır ve vektör veritabanına kaydedilir.
Bash
uv run python ingest.py
# Çıktı: ✅ Web sayfaları başarıyla yüklendi ve Chroma veritabanına eklendi!
4. Uygulamayı BaşlatmaVeri tabanı hazırlandıktan sonra RAG asistanını başlatabilirsiniz.
Bash
uv run python feed.py
Welcome to the EU AI Act Assistant! (type 'quit' to exit)

Your question: What risk categories does the EU AI Act define?

Answer: Based on the provided context, the EU AI Act defines or refers to the following risk categories:

1.  **High-risk AI systems**: This category includes AI systems that pose significant risks, such as emotion recognition systems (unless prohibited) and certain biometric systems. However, biometric systems used solely for cybersecurity and personal data protection measures are explicitly *not* considered high-risk.
2.  **Systemic risks**: These are risks specifically stemming from AI models, which the AI Act addresses through measures like model evaluations, reporting serious incidents, and ensuring adequate cybersecurity.
3.  **Risks to fundamental rights**: These are specific risks that AI systems might pose to fundamental rights, which must be considered as required by the Regulation.

The context also implicitly distinguishes a category of AI systems that are "not high-risk," specifically mentioning biometric systems intended for cybersecurity and personal data protection, though it does not assign a formal name to this category.

Your question: What is a “high-risk AI system”? Give 2 examples.                                              

Answer: A "high-risk AI system" is defined as an AI system that has a significant harmful impact on the health, safety, and fundamental rights of persons in the Union. The classification of AI systems as high-risk is intended to be limited to those with such significant impacts.

Based on the provided context, two examples of AI systems that are classified as high-risk are:

1.  **Emotion recognition systems** that are not prohibited under the Regulation.
2.  **Biometric systems**, with the notable exception of those intended to be used *solely* for the purpose of enabling cybersecurity and personal data protection measures, which are explicitly stated as *not* being considered high-risk. Therefore, biometric systems used for other purposes would fall under the high-risk category.

Your question: What are the transparency obligations for general-purpose AI (GPAI) models?

Answer: Based on the provided context, providers of general-purpose AI (GPAI) models have the following transparency obligations:

1.  **Technical Documentation**: Providers must draw up and keep up-to-date the technical documentation of the model. This documentation must include its training and testing process, the results of its evaluation, and, at a minimum, the information set out in Annex XI. This documentation must be provided, upon request, to the AI Office and the national competent authorities.
2.  **Information and Documentation for Downstream Providers**: Providers must draw up, keep up-to-date, and make available information and documentation to providers of AI systems who intend to integrate the general-purpose AI model into their own AI systems. This information and documentation is intended to:
    *   Enable providers of AI systems to have a good understanding of the capabilities and limitations of the general-purpose AI model.
    *   Enable providers of AI systems to comply with their obligations pursuant to the Regulation.

It is important to note that these obligations are to be fulfilled without prejudice to the need to observe and protect intellectual property rights and confidential business information or trade secrets in accordance with Union and national law.

Your question: How do enforcement and penalties work?

Answer: Enforcement and penalties under the EU AI Act are structured as follows:

**1. Enforcement Authorities and Scope:**

*   **AI Office (Commission):**
    *   **Primary Role:** Supervises and enforces obligations for **providers of general-purpose AI (GPAI) models** (Article 88 AI Act).
    *   **Exceptional Role:** Enforces obligations for providers of AI systems based on GPAI models if the provider of the model and the system are the same (Article 75 (1) AI Act).
    *   **Support Role:** Supports relevant market surveillance authorities of the Member States in their enforcement of requirements for AI systems (Article 75 (2) and (3) AI Act).
    *   **Initiation of Investigations:** Can investigate possible infringements of GPAI model rules on its own initiative (following monitoring activities) or upon request from market surveillance authorities (Recital 162).
*   **Member State Market Surveillance Authorities:**
    *   Responsible for enforcing the requirements for AI systems generally.
    *   Any natural or legal person with grounds to consider an infringement of the Regulation can lodge a complaint with the relevant market surveillance authority (Recital 170).

**2. Enforcement Powers of the AI Office:**

The AI Office is endowed with several powers to ensure compliance (Recital 162, first paragraph):

*   **Request Information:** Powers to request information (Article 91 AI Act).
*   **Conduct Evaluations:** Powers to conduct evaluations of general-purpose AI models (Article 92 AI Act).
*   **Request Measures:** Powers to request specific measures from providers, including implementing risk mitigations (e.g., for systemic risks) and recalling the model from the market (Article 93 AI Act).
*   **Monitor and Investigate:** Ability to carry out all necessary actions to monitor the effective implementation of the Regulation regarding GPAI models and investigate possible infringements (Recital 162).

**3. Penalties:**

*   **Fines:** The AI Office (on behalf of the Commission) has the power to impose fines (Recital 169).
    *   **Maximum Amount:** Up to **3% of the global annual turnover** or **15 million Euros**, whichever is higher (Article 101 AI Act).
    *   **Scope:** These fines are for infringements of obligations on providers of general-purpose AI models, including the failure to comply with measures requested by the Commission.
*   **Proportionality:** Fines are subject to appropriate limitation periods and the principle of proportionality (Recital 169).

**4. Judicial Review:**

*   All decisions taken by the Commission under the AI Act are subject to review by the Court of Justice of the European Union (CJEU) in accordance with the Treaty on the Functioning of the European Union (TFEU), including the unlimited jurisdiction of the Court of Justice with regard to penalties pursuant to Article 261 TFEU (Recital 169).

In summary, the AI Office, as part of the Commission, holds significant powers for the supervision and enforcement of general-purpose AI models, including investigative capabilities, the ability to mandate corrective measures, and the authority to levy substantial fines. Member State authorities manage enforcement for other AI systems, with the AI Office providing support.

Your question: What is the timeline for the Act’s application phases?

Answer: The EU AI Act has a phased application timeline, with different provisions becoming applicable at various stages:

*   **1 August 2024**: The AI Act officially **entered into force**.
*   **2 February 2025**:
    *   **Prohibitions** on certain AI practices became applicable.
    *   **AI literacy obligations** entered into application.
    *   **General provisions** of the Regulation also began to apply.
*   **2 May 2025**:
    *   **Codes of practice** (e.g., for GPAI models) should be ready to enable providers to demonstrate compliance. (The Commission expects to finalise the Code of Practice by April 2025).
*   **2 August 2025**:
    *   **Governance rules** became applicable.
    *   **Obligations for General-Purpose AI (GPAI) models** became applicable.
    *   Provisions concerning **notified bodies** and the **governance structure** became applicable to ensure the conformity assessment system is operational.
    *   Provisions on **penalties** should apply.
*   **2 August 2026**:
    *   The AI Act will be **fully applicable**.
    *   By this date, Member States should have laid down and notified to the Commission the rules on penalties, including administrative fines, and ensured their proper and effective implementation.
*   **2 August 2027**:
    *   An **extended transition period** applies for the rules concerning **high-risk AI systems embedded into regulated products**.

Your question: q
👋 Goodbye!
