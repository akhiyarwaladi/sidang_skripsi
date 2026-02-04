# ANALISIS KOMPREHENSIF PROPOSAL SKRIPSI
## "Analisis Sentimen Ulasan Pengguna Aplikasi Duolingo Menggunakan IndoBERTweet dan Pemodelan Topik BERTopic"

**Mahasiswa:** Muhammad Farhan Hadrawi
**Tanggal Analisis:** 4 Januari 2026
**Disusun untuk:** Persiapan Seminar Proposal

---

# DAFTAR ISI

1. [Ringkasan Eksekutif](#1-ringkasan-eksekutif)
2. [State-of-the-Art Research](#2-state-of-the-art-research)
3. [Analisis IndoBERTweet](#3-analisis-indobertweet)
4. [Analisis BERTopic](#4-analisis-bertopic)
5. [Gap Analysis & Critical Issues](#5-gap-analysis--critical-issues)
6. [Pertanyaan Penguji dengan Solusi](#6-pertanyaan-penguji-dengan-solusi)
7. [Rekomendasi Metodologi](#7-rekomendasi-metodologi)
8. [Referensi Lengkap](#8-referensi-lengkap)

---

# 1. RINGKASAN EKSEKUTIF

## 1.1 Tentang Penelitian

Penelitian ini mengkombinasikan:
- **IndoBERTweet** untuk analisis sentimen ulasan Duolingo
- **BERTopic** untuk pemodelan topik dari ulasan tersebut

## 1.2 Penelitian Sejenis yang Sudah Ada

| Penelitian | Metode | Hasil | Referensi |
|------------|--------|-------|-----------|
| Sentiment Analysis & Topic Modeling Duolingo (2024) | LDA + ML | Akurasi 90.51% | [IEEE Xplore](https://ieeexplore.ieee.org/document/10913140/) |
| Duolingo vs Babbel Analysis (2025) | Mixed-methods, Network Analysis | Comprehensive insights | [Frontiers](https://www.frontiersin.org/journals/computer-science/articles/10.3389/fcomp.2025.1569058/full) |
| BERTopic + RoBERTa Framework (2025) | Topic + Sentiment Integration | State-of-the-art | [PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC11946272/) |

## 1.3 Isu Kritis Utama

1. **Domain Mismatch**: IndoBERTweet dilatih pada Twitter, bukan app review
2. **Novelty Question**: Penelitian serupa sudah ada dengan LDA (akurasi 90.51%)
3. **Technical Challenges**: Memory issues BERTopic, overfitting IndoBERTweet

---

# 2. STATE-OF-THE-ART RESEARCH

## 2.1 Kombinasi Topic Modeling + Sentiment Analysis

### 2.1.1 BERTopic-SKEP Framework (2025)
Framework terbaru yang mengintegrasikan BERTopic dengan SKEP sentiment analysis untuk analisis kebijakan publik. Mengatasi limitasi LDA dalam pemrosesan teks pendek dengan semantic embeddings.

**Sumber:** [Nature Scientific Reports](https://www.nature.com/articles/s41598-025-30319-4)

### 2.1.2 BERTopic + RoBERTa (2025)
Metode user requirement mining yang menggabungkan BERTopic untuk ekstraksi topik dan RoBERTa untuk analisis sentimen, memfasilitasi linked analysis antara emosi pengguna dan topik yang teridentifikasi.

**Sumber:** [PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC11946272/)

### 2.1.3 Joint Sentiment-Topic (JST) Models
Model TDS (Topic Document Sentence) berbasis JST dan LDA yang mengasosiasikan sentiment labels dengan dokumen, topics dengan sentiment labels.

**Sumber:** [MDPI Applied Sciences](https://www.mdpi.com/2076-3417/11/23/11091)

## 2.2 Sentiment Analysis untuk App Reviews

### 2.2.1 LLM-Based Approaches (2024)
Llama-70B menunjukkan performa comparable dengan GPT family untuk feature-specific sentiment analysis pada app reviews.

**Sumber:** [arXiv](https://arxiv.org/abs/2409.07162)

### 2.2.2 Deep Learning untuk Google Play Reviews
LSTM outperform ANN dan SVM dengan akurasi 80-90% untuk sentiment analysis app reviews.

**Sumber:** [Springer](https://link.springer.com/article/10.1007/s11042-024-19185-w)

## 2.3 BERTopic untuk Bahasa Indonesia

### 2.3.1 BERTopic Indonesian Biodiversity (2024)
Studi foundational untuk kategorisasi topik bahasa Indonesia menggunakan BERTopic. Model 5 dengan coherence score 0.7733 adalah optimal.

**Sumber:** [ECTI-CIT](https://ph01.tci-thaijo.org/index.php/ecticit/article/view/255058)

### 2.3.2 Indonesian News Topic Modeling
BERTopic menunjukkan keunggulan dibanding LDA dalam generating coherent dan interpretable topics untuk data berita Indonesia.

**Sumber:** [IEEE Xplore](https://ieeexplore.ieee.org/document/10903779/)

---

# 3. ANALISIS INDOBERTWEET

## 3.1 Spesifikasi Model

| Aspek | Detail |
|-------|--------|
| **Arsitektur** | BERT-base-uncased |
| **Attention Heads** | 12 |
| **Hidden Layers** | 12 |
| **Parameters** | ~110.6 juta |
| **Training Data** | 26 juta tweets, 409 juta kata |
| **Training Period** | Desember 2019 - Desember 2020 |
| **Domain** | Ekonomi, kesehatan, pendidikan, politik |
| **Publikasi** | EMNLP 2021 |

**Sumber:** [GitHub IndoBERTweet](https://github.com/indolem/IndoBERTweet), [arXiv](https://arxiv.org/abs/2109.04607)

## 3.2 Perbandingan Performa IndoBERTweet vs IndoBERT

| Dataset/Task | IndoBERTweet | IndoBERT | Selisih |
|--------------|--------------|----------|---------|
| Electric Vehicle Sentiment | **82.40%** (acc) | 75.98% (acc) | +6.42% |
| Student Feedback Multilabel | **0.8462** (F1) | 0.8243 (F1) | +0.0219 |
| Racing Circuit Sentiment | **86%** (acc) | - | - |
| Tapera Policy | **89.73%** (acc) | - | - |

**Kesimpulan:** IndoBERTweet secara konsisten outperform IndoBERT untuk teks sosial media.

**Sumber:** [Antivirus Journal](https://ejournal.unisbablitar.ac.id/index.php/antivirus/article/view/4416), [JOSH Journal](https://ejurnal.seminar-id.com/index.php/josh/article/view/6505)

## 3.3 Kelebihan IndoBERTweet

1. **Domain-Specific Training**: Dilatih khusus pada Twitter Indonesia
2. **Effective Vocabulary Initialization**: 5x lebih cepat dalam pretraining
3. **Handles Informal Language**: Lebih baik dalam menangani bahasa informal
4. **Strong Performance**: F1-score hingga 89.97% untuk analisis sentimen

## 3.4 Kekurangan & Limitasi

| Limitasi | Deskripsi | Impact |
|----------|-----------|--------|
| **Overfitting** | F1 training 0.97 vs validation 0.84 | High |
| **Code-Mixing Issues** | Kesulitan dengan campuran bahasa | Medium |
| **Domain Specificity** | Optimal untuk Twitter, bukan app review | **Critical** |
| **Limited Labeled Data** | Data berlabel Indonesia terbatas | Medium |
| **Regional Language** | Tidak optimal untuk bahasa daerah | Low |

**Sumber:** [Springer](https://link.springer.com/article/10.1007/s13278-025-01439-6), [ResearchGate](https://www.researchgate.net/publication/357122364)

## 3.5 Rekomendasi Fine-Tuning

| Parameter | Recommended Value | Notes |
|-----------|-------------------|-------|
| Learning Rate | 2e-5 atau 3e-5 | Terlalu besar akan destroy pre-trained weights |
| Epochs | 2-4 | BERT sudah encode banyak informasi |
| Batch Size | 16-32 | Tergantung hardware |
| Dropout | 0.1-0.3 | Untuk mengurangi overfitting |
| Optimizer | AdamW | Dengan weight decay |

**Sumber:** [LinkedIn](https://www.linkedin.com/advice/0/what-best-practices-fine-tuning-bert-sentiment), [GeeksforGeeks](https://www.geeksforgeeks.org/nlp/fine-tuning-bert-model-for-sentiment-analysis/)

---

# 4. ANALISIS BERTOPIC

## 4.1 Arsitektur BERTopic

```
Document → Embedding (BERT/Sentence-Transformers)
        → Dimensionality Reduction (UMAP)
        → Clustering (HDBSCAN)
        → Topic Representation (c-TF-IDF)
```

## 4.2 Kelebihan BERTopic

| Kelebihan | Deskripsi |
|-----------|-----------|
| **Automatic Topic Discovery** | Tidak perlu menentukan jumlah topik |
| **Semantic Understanding** | Menangkap makna semantik lebih dalam dari LDA |
| **Modular Architecture** | Komponen dapat diganti sesuai kebutuhan |
| **Multilingual Support** | Mendukung 50+ bahasa termasuk Indonesia |
| **Hierarchical Topic Reduction** | Dapat mengurangi topik secara hierarkis |

## 4.3 Kekurangan & Limitasi BERTopic

| Limitasi | Deskripsi | Solusi |
|----------|-----------|--------|
| **Memory Issues** | Out-of-memory pada dataset besar | Gunakan low_memory mode, batch processing |
| **Too Many Topics** | Sering menghasilkan >50 topik | Gunakan hierarchical reduction, tune min_topic_size |
| **Single Topic Assignment** | 1 dokumen = 1 topik | Pertimbangkan soft clustering |
| **Slow on Large Data** | Embedding phase lambat | GPU acceleration, async processing |
| **Short Text Issues** | Kurang optimal untuk teks sangat pendek | Aggregate reviews, use appropriate embeddings |

**Sumber:** [BERTopic Docs](https://maartengr.github.io/BERTopic/), [GitHub Issues](https://github.com/MaartenGr/BERTopic/issues/1642)

## 4.4 Hyperparameter Tuning Guidelines

### UMAP Parameters
| Parameter | Default | Recommended Range | Effect |
|-----------|---------|-------------------|--------|
| n_neighbors | 15 | 10-30 | Local vs global structure |
| n_components | 5 | 5-10 | Dimensionality |
| min_dist | 0.0 | 0.0 (jangan ubah) | Cluster density |
| metric | cosine | cosine | Distance measure |

### HDBSCAN Parameters
| Parameter | Default | Recommended Range | Effect |
|-----------|---------|-------------------|--------|
| min_cluster_size | 10 | Depends on data size | Minimum topic size |
| min_samples | None | 5-15 | Core point density |
| cluster_selection_method | eom | leaf/eom | Topic granularity |

**Sumber:** [BERTopic Parameter Tuning](https://maartengr.github.io/BERTopic/getting_started/parameter%20tuning/parametertuning.html)

## 4.5 BERTopic vs Alternatif

| Model | Coherence | Diversity | Speed | Interpretability |
|-------|-----------|-----------|-------|------------------|
| **BERTopic** | High | High | Medium | High |
| **FASTopic** | Higher | Higher | **Fast** | High |
| **LDA** | Medium | Medium | Fast | Medium |
| **Top2Vec** | High | Medium | Medium | High |

**FASTopic** (NeurIPS 2024) menunjukkan performa lebih baik dari BERTopic dalam coherence, diversity, dan speed.

**Sumber:** [FASTopic GitHub](https://github.com/BobXWu/FASTopic), [Towards Data Science](https://towardsdatascience.com/topic-modelling-in-business-intelligence-fastopic-and-bertopic-in-code-2d3949260a37/)

---

# 5. GAP ANALYSIS & CRITICAL ISSUES

## 5.1 Domain Mismatch Problem

### Masalah
IndoBERTweet dilatih pada **Twitter data** dengan karakteristik:
- Teks pendek (≤280 karakter)
- Hashtags, mentions, URLs
- Bahasa sangat informal
- Topik: ekonomi, kesehatan, pendidikan, politik

Google Play Store reviews memiliki karakteristik **berbeda**:
- Bisa lebih panjang
- Tanpa hashtags/mentions
- Lebih terstruktur
- Fokus pada fitur aplikasi

### Evidence
Penelitian cross-domain sentiment analysis menunjukkan:
> "Domain adaptation is an important part of transfer learning, which aims to map data from different source and target domains into a common feature space."

**Sumber:** [PMC Cross-Domain](https://pmc.ncbi.nlm.nih.gov/articles/PMC10458120/)

### Solusi yang Direkomendasikan
1. **Further Fine-tuning**: Fine-tune IndoBERTweet pada sample app reviews
2. **Domain Adaptation**: Gunakan teknik seperti KL Divergence untuk alignment
3. **Alternative Model**: Pertimbangkan IndoBERT yang lebih general
4. **Hybrid Approach**: Ensemble IndoBERTweet + IndoBERT

## 5.2 Existing Research Gap

### Penelitian yang Sudah Ada
1. **IEEE 2024**: Sentiment Analysis + Topic Modeling Duolingo dengan LDA (90.51% accuracy)
2. **Frontiers 2025**: Duolingo vs Babbel comprehensive analysis

### Novelty yang Perlu Dijustifikasi
| Aspek | Existing Research | Proposed Research | Novelty? |
|-------|-------------------|-------------------|----------|
| Sentiment Method | Traditional ML | IndoBERTweet | Yes |
| Topic Modeling | LDA | BERTopic | Yes |
| Language | English | Indonesian | Yes |
| Integration | Sequential | ? | Unclear |

## 5.3 Technical Challenges

### Challenge 1: Data Labeling
- Perlu inter-rater reliability (Krippendorff's α ≥ 0.7)
- Manual labeling time-consuming
- Rating tidak selalu reflect sentiment

### Challenge 2: Class Imbalance
- App reviews biasanya majority positive
- Need stratified sampling atau oversampling

### Challenge 3: Code-Mixing
- Duolingo users mix Indonesian + English
- IndoBERTweet struggles dengan extensive code-mixing

---

# 6. PERTANYAAN PENGUJI DENGAN SOLUSI

## KATEGORI A: METODOLOGI DAN JUSTIFIKASI

### Pertanyaan A1 [CRITICAL]
**"Mengapa memilih IndoBERTweet yang dilatih pada data Twitter, padahal data penelitian Anda adalah review Google Play Store? Bagaimana Anda mengatasi domain mismatch ini?"**

#### Expected Answer (Solusi)
```
Mahasiswa seharusnya menjawab:

1. ACKNOWLEDGE THE GAP:
   "Saya menyadari ada domain mismatch antara Twitter dan app reviews."

2. JUSTIFICATION:
   - IndoBERTweet tetap relevan karena:
     a) Bahasa informal Indonesia mirip di kedua platform
     b) Review app juga menggunakan bahasa kasual
     c) IndoBERTweet outperform IndoBERT untuk teks informal

3. MITIGATION STRATEGY:
   - Fine-tuning pada sample app reviews (500-1000 labeled reviews)
   - Validasi dengan subset test
   - Bandingkan dengan baseline (IndoBERT, traditional ML)

4. SUPPORTING EVIDENCE:
   - Cite: Cross-domain sentiment research menunjukkan BERT-based
     models dapat beradaptasi dengan fine-tuning minimal
```

**Referensi untuk jawaban:** [Cross-Domain Sentiment](https://www.tandfonline.com/doi/full/10.1080/09540091.2021.1912711)

---

### Pertanyaan A2 [CRITICAL]
**"Sudah ada penelitian 'Sentiment Analysis and Topic Modeling for Duolingo Application on Google Play Store' (IEEE 2024) dengan LDA yang mencapai akurasi 90.51%. Apa novelty penelitian Anda dibandingkan penelitian tersebut?"**

#### Expected Answer (Solusi)
```
Novelty yang harus disampaikan:

1. LANGUAGE NOVELTY:
   - Penelitian existing fokus pada English reviews
   - Penelitian ini fokus pada Indonesian reviews (under-explored)

2. METHOD NOVELTY:
   - LDA adalah probabilistic model tradisional
   - BERTopic menggunakan neural embeddings (semantic understanding lebih baik)
   - IndoBERTweet adalah state-of-the-art untuk Indonesian social text

3. INTEGRATION NOVELTY:
   - Propose framework integrasi topic-sentiment analysis
   - Topic-wise sentiment distribution (sentimen per topik)

4. EXPECTED IMPROVEMENT:
   - BERTopic terbukti lebih baik dari LDA dalam coherence dan diversity
   - Cite: "BERTopic outperforms LDA on multiple benchmark datasets"

5. PRACTICAL CONTRIBUTION:
   - Insights untuk developer Duolingo tentang user Indonesia
```

**Referensi:** [IEEE Duolingo](https://ieeexplore.ieee.org/document/10913140/), [BERTopic vs LDA](https://pmc.ncbi.nlm.nih.gov/articles/PMC9120935/)

---

### Pertanyaan A3
**"Mengapa tidak menggunakan IndoBERT biasa yang dilatih pada teks formal, mengingat review Play Store cenderung lebih formal dibanding tweet?"**

#### Expected Answer (Solusi)
```
1. COUNTER-ARGUMENT:
   - App reviews TIDAK selalu formal
   - Banyak menggunakan bahasa kasual, singkatan, emoji

2. EMPIRICAL EVIDENCE:
   - IndoBERTweet vs IndoBERT pada Electric Vehicle sentiment:
     * IndoBERTweet: 82.40% accuracy
     * IndoBERT: 75.98% accuracy
   - Gap: 6.42% favor IndoBERTweet

3. PROPOSED VALIDATION:
   - Akan melakukan comparative study:
     * IndoBERTweet
     * IndoBERT
     * Baseline (SVM, Naive Bayes)
   - Pilih model terbaik berdasarkan hasil

4. FALLBACK PLAN:
   - Jika IndoBERT lebih baik, akan adjust methodology
```

**Referensi:** [IndoBERTweet vs IndoBERT](https://ejournal.unisbablitar.ac.id/index.php/antivirus/article/view/4416)

---

### Pertanyaan A4
**"BERTopic diketahui menghasilkan banyak topik (bisa >50). Bagaimana strategi Anda untuk hierarchical topic reduction agar hasilnya interpretable?"**

#### Expected Answer (Solusi)
```
1. PARAMETER TUNING:
   - Increase min_topic_size (default 10 → 20-50)
   - Adjust HDBSCAN min_cluster_size

2. HIERARCHICAL REDUCTION:
   - Gunakan BERTopic.reduce_topics(nr_topics=10)
   - Hierarchical topic modeling untuk group similar topics

3. MANUAL CURATION:
   - Post-processing: merge similar topics
   - Domain expert validation

4. COHERENCE-BASED SELECTION:
   - Evaluate dengan C_V coherence score
   - Target coherence > 0.5

5. VISUALIZATION:
   - Topic hierarchy dendrogram
   - Intertopic distance map
```

**Referensi:** [BERTopic Hierarchical](https://maartengr.github.io/BERTopic/getting_started/hierarchicaltopics/hierarchicaltopics.html)

---

## KATEGORI B: PERTANYAAN TEKNIS

### Pertanyaan B1
**"Berapa jumlah data review yang akan Anda kumpulkan? BERTopic memiliki masalah out-of-memory pada dataset besar. Bagaimana antisipasi Anda?"**

#### Expected Answer (Solusi)
```
1. DATA SIZE PLANNING:
   - Target: 10,000 - 50,000 reviews
   - Justifikasi: Sufficient untuk BERTopic tanpa memory issues

2. MEMORY OPTIMIZATION:
   - Gunakan low_memory=True pada UMAP
   - Batch processing untuk embedding
   - Pre-compute embeddings sebelum clustering

3. HARDWARE CONSIDERATION:
   - Minimum RAM: 16GB untuk <50K docs
   - GPU acceleration untuk embedding phase

4. SAMPLING STRATEGY:
   - Stratified sampling berdasarkan rating
   - Time-based sampling (recent vs old reviews)

5. CODE EXAMPLE:
   from bertopic import BERTopic
   from umap import UMAP

   umap_model = UMAP(n_neighbors=15, n_components=5,
                     min_dist=0.0, metric='cosine',
                     low_memory=True)

   topic_model = BERTopic(umap_model=umap_model)
```

**Referensi:** [BERTopic Scalability](https://bertopic.com/how-scalable-is-bertopic-for-large-datasets/)

---

### Pertanyaan B2
**"IndoBERTweet memiliki masalah overfitting (F1 training 0.97 vs validation 0.84). Bagaimana strategi cross-validation Anda?"**

#### Expected Answer (Solusi)
```
1. K-FOLD CROSS-VALIDATION:
   - Gunakan 5-fold atau 10-fold CV
   - Stratified split untuk maintain class distribution

2. REGULARIZATION:
   - Dropout rate: 0.1-0.3
   - Weight decay dalam AdamW optimizer
   - Early stopping berdasarkan validation loss

3. DATA AUGMENTATION:
   - Back-translation
   - Synonym replacement
   - Random insertion/deletion

4. HYPERPARAMETER SEARCH:
   - Grid search untuk learning rate, batch size
   - Gunakan Optuna untuk Bayesian optimization

5. MONITORING:
   - Track training vs validation loss
   - Stop jika validation loss naik 3 epoch berturut-turut

6. REPORTING:
   - Report mean ± std dari cross-validation
   - Confusion matrix per fold
```

**Referensi:** [BERT Fine-tuning](https://www.researchgate.net/publication/333102203_How_to_Fine-Tune_BERT_for_Text_Classification)

---

### Pertanyaan B3
**"Bagaimana Anda menangani code-mixing (Bahasa Indonesia + Inggris) dalam review Duolingo, mengingat ini adalah aplikasi bahasa?"**

#### Expected Answer (Solusi)
```
1. PREPROCESSING APPROACH:
   - Detect language per sentence/word
   - Normalize to single language jika possible

2. MODEL CONSIDERATION:
   - IndoBERTweet sudah handle some code-mixing
   - Alternatif: Gunakan multilingual model (mBERT, XLM-R)

3. HYBRID APPROACH:
   - Segment review berdasarkan language
   - Process each segment dengan appropriate model

4. EMPIRICAL TESTING:
   - Measure performance pada code-mixed subset
   - Compare with monolingual reviews

5. LIMITATIONS ACKNOWLEDGMENT:
   - Acknowledge code-mixing sebagai limitation
   - Report separate metrics untuk mixed vs pure Indonesian
```

**Referensi:** [Code-Mixing NLP](https://aclanthology.org/D19-5554.pdf)

---

### Pertanyaan B4
**"BERTopic membatasi satu dokumen ke satu topik. Bagaimana jika satu review membahas multiple aspects (harga, fitur, bug)?"**

#### Expected Answer (Solusi)
```
1. SENTENCE-LEVEL ANALYSIS:
   - Split review menjadi sentences
   - Apply BERTopic per sentence
   - Aggregate topics per review

2. ASPECT-BASED APPROACH:
   - Combine dengan Aspect-Based Sentiment Analysis (ABSA)
   - Extract (aspect, sentiment) pairs

3. SOFT CLUSTERING:
   - Modify HDBSCAN untuk soft clustering
   - Get topic probability distribution per document

4. POST-HOC ANALYSIS:
   - Identify multi-topic reviews
   - Manual categorization untuk validation

5. ALTERNATIVE MODEL:
   - Consider probabilistic topic models (LDA) untuk comparison
   - LDA naturally assigns multiple topics

6. HYBRID SOLUTION:
   - BERTopic untuk primary topic
   - Secondary analysis untuk additional aspects
```

**Referensi:** [ABSA for App Reviews](https://link.springer.com/article/10.1007/s10515-023-00397-7)

---

## KATEGORI C: DATASET DAN PREPROCESSING

### Pertanyaan C1
**"Apakah Anda akan memfilter review berdasarkan tanggal? Duolingo mengalami update besar di 2023 yang mengubah sentiment pengguna secara drastis."**

#### Expected Answer (Solusi)
```
1. TEMPORAL AWARENESS:
   - Ya, akan filter berdasarkan tanggal
   - Focus pada reviews setelah major update (Q1 2023+)

2. TEMPORAL ANALYSIS:
   - Compare sentiment before vs after update
   - Track topic evolution over time

3. ANNOTATION:
   - Include timestamp sebagai metadata
   - Analyze sentiment trends

4. JUSTIFICATION:
   - Outdated reviews tidak reflect current state
   - User behavior berbeda pre/post update

5. METHODOLOGY:
   - Collect reviews dari 2023-2025
   - Option: Separate analysis per period
```

**Referensi:** [Relative Insight Duolingo](https://relativeinsight.com/tracking-what-users-think-duolingo-app-review-analysis/)

---

### Pertanyaan C2
**"Bagaimana Anda menangani review sangat pendek (1-2 kata) yang umum di Play Store? BERTopic tidak optimal untuk very short text."**

#### Expected Answer (Solusi)
```
1. FILTERING:
   - Set minimum length threshold (e.g., 10 words)
   - Document filtering criteria dalam methodology

2. AGGREGATION:
   - Group very short reviews dengan same rating/date
   - Treat aggregated text sebagai single document

3. EMBEDDING STRATEGY:
   - Use sentence-transformers yang handle short text
   - 'paraphrase-multilingual-MiniLM-L12-v2' for short text

4. STATISTICAL REPORTING:
   - Report distribution of review lengths
   - Analyze removed reviews

5. SENSITIVITY ANALYSIS:
   - Test dengan different thresholds
   - Report impact on results
```

**Referensi:** [BERTopic Short Text](https://arxiv.org/pdf/2402.03067)

---

### Pertanyaan C3
**"Apakah rating (1-5 bintang) akan digunakan sebagai ground truth sentiment? Bagaimana menangani inkonsistensi antara teks dan rating?"**

#### Expected Answer (Solusi)
```
1. LABELING STRATEGY:
   Option A: Rating-based (with mapping)
   - 1-2 stars = Negative
   - 3 stars = Neutral
   - 4-5 stars = Positive

   Option B: Manual labeling (recommended)
   - Human annotators label berdasarkan teks
   - Rating sebagai reference only

2. HANDLING INCONSISTENCY:
   - Identify mismatch cases (positive text + low rating)
   - Analyze reasons (update issues, response to developer)
   - Report percentage of inconsistent cases

3. VALIDATION:
   - Inter-rater reliability (Cohen's Kappa ≥ 0.6)
   - Krippendorff's Alpha ≥ 0.7

4. HYBRID APPROACH:
   - Use rating untuk initial label
   - Manual verification untuk ambiguous cases
   - Separate analysis untuk inconsistent cases
```

**Referensi:** [App Review Labeling](https://www.nature.com/articles/s41598-025-28799-5)

---

### Pertanyaan C4
**"Bagaimana proses preprocessing yang akan Anda lakukan untuk review berbahasa Indonesia?"**

#### Expected Answer (Solusi)
```
PREPROCESSING PIPELINE:

1. TEXT CLEANING:
   - Remove URLs, email addresses
   - Remove special characters (keep punctuation)
   - Normalize whitespace

2. CASE NORMALIZATION:
   - Convert to lowercase

3. SLANG NORMALIZATION:
   - Dictionary-based replacement
   - "gak" → "tidak", "bgt" → "banget", etc.
   - Use: https://github.com/nasalsabila/kamus-alay

4. STOPWORD REMOVAL:
   - Sastrawi stopword list
   - Keep domain-relevant words

5. STEMMING (OPTIONAL):
   - Sastrawi stemmer (Nazief-Adriani algorithm)
   - Note: BERT-based models may not need stemming

6. EMOJI HANDLING:
   - Option A: Remove emojis
   - Option B: Convert to text (😊 → "happy")

7. TOKENIZATION:
   - WordPiece tokenizer (built into BERT)

CODE:
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory

# Stemmer
factory = StemmerFactory()
stemmer = factory.createStemmer()

# Stopword Remover
stop_factory = StopWordRemoverFactory()
stopword = stop_factory.createStopWordRemover()
```

**Referensi:** [Indonesian Preprocessing](https://cindyhosea.medium.com/text-pre-processing-in-bahasa-indonesia-6895154532db), [Sastrawi](https://medium.com/@andikahfi98/preprocessing-text-data-in-python-using-nltk-and-sastrawi-ef6b7450b7db)

---

## KATEGORI D: ANALISIS DAN KONTRIBUSI

### Pertanyaan D1
**"Apa expected output dari kombinasi sentiment + topic? Apakah topic-wise sentiment distribution seperti framework BERTopic-SKEP?"**

#### Expected Answer (Solusi)
```
EXPECTED OUTPUTS:

1. TOPIC-SENTIMENT MATRIX:
   | Topic | Positive | Neutral | Negative | Total |
   |-------|----------|---------|----------|-------|
   | Gamification | 450 | 50 | 20 | 520 |
   | Bugs/Errors | 30 | 20 | 200 | 250 |
   | Pricing | 100 | 80 | 150 | 330 |

2. TOPIC DESCRIPTIONS:
   - Top keywords per topic
   - Representative documents
   - Topic coherence scores

3. SENTIMENT TRENDS:
   - Overall sentiment distribution
   - Sentiment per rating level

4. INSIGHTS:
   - Most positive aspects (gamification, lessons)
   - Most negative aspects (bugs, ads, pricing)
   - Neutral discussions (feature requests)

5. VISUALIZATION:
   - Topic hierarchy
   - Sentiment heatmap per topic
   - Temporal analysis

6. ACTIONABLE RECOMMENDATIONS:
   - Priority areas untuk improvement
   - User satisfaction drivers
```

**Referensi:** [BERTopic-SKEP](https://www.nature.com/articles/s41598-025-30319-4)

---

### Pertanyaan D2
**"Bagaimana hasil penelitian ini akan berkontribusi praktis bagi pengembang Duolingo atau aplikasi edukasi lainnya?"**

#### Expected Answer (Solusi)
```
PRACTICAL CONTRIBUTIONS:

1. USER FEEDBACK INSIGHTS:
   - Identify pain points pengguna Indonesia
   - Prioritize feature development

2. CULTURAL ADAPTATION:
   - Indonesian-specific preferences
   - Local content recommendations

3. QUALITY IMPROVEMENT:
   - Bug patterns identification
   - UX improvement areas

4. COMPETITIVE ANALYSIS:
   - Benchmark dengan competitors
   - Unique selling points

5. METHODOLOGICAL FRAMEWORK:
   - Reusable pipeline untuk app lain
   - Indonesian NLP best practices

6. ACADEMIC CONTRIBUTION:
   - IndoBERTweet validation on new domain
   - BERTopic application untuk Indonesian text

7. BUSINESS VALUE:
   - Reduce manual review analysis time
   - Data-driven decision making
```

---

### Pertanyaan D3
**"Apakah Anda akan membandingkan performa IndoBERTweet dengan baseline seperti LSTM, Naive Bayes, atau IndoBERT?"**

#### Expected Answer (Solusi)
```
COMPARATIVE ANALYSIS PLAN:

1. BASELINE MODELS:
   - Naive Bayes (TF-IDF features)
   - SVM (TF-IDF features)
   - LSTM (word embeddings)
   - IndoBERT (general Indonesian)

2. EVALUATION METRICS:
   - Accuracy
   - Precision, Recall, F1 (macro & weighted)
   - Confusion Matrix
   - ROC-AUC

3. STATISTICAL TESTING:
   - McNemar's test untuk significance
   - 95% confidence intervals

4. ABLATION STUDY:
   - With/without preprocessing
   - Different embedding models

5. EXPECTED TABLE:
   | Model | Accuracy | F1-Macro | F1-Weighted |
   |-------|----------|----------|-------------|
   | Naive Bayes | ~75% | ~0.72 | ~0.74 |
   | SVM | ~78% | ~0.75 | ~0.77 |
   | LSTM | ~80% | ~0.78 | ~0.79 |
   | IndoBERT | ~82% | ~0.80 | ~0.81 |
   | IndoBERTweet | ~85% | ~0.83 | ~0.84 |
```

---

## KATEGORI E: PERTANYAAN KRITIS

### Pertanyaan E1 [CHALLENGING]
**"Penelitian sejenis (2025) menggunakan LSTM mencapai akurasi 80-90% untuk Google Play review. Apa justifikasi menggunakan model yang lebih kompleks seperti IndoBERTweet?"**

#### Expected Answer (Solusi)
```
JUSTIFICATION:

1. PERFORMANCE CEILING:
   - LSTM 80-90% adalah good, tapi tidak state-of-the-art
   - BERT-based models consistently outperform LSTM

2. FEATURE RICHNESS:
   - BERT captures contextual embeddings
   - LSTM limited to sequential patterns

3. TRANSFER LEARNING:
   - IndoBERTweet pre-trained on massive data
   - LSTM requires training from scratch

4. PRACTICAL ADVANTAGES:
   - Better generalization
   - Easier fine-tuning
   - Active research community

5. COMPUTATIONAL TRADE-OFF:
   - Acknowledge: BERT more resource-intensive
   - Mitigation: Use smaller batch, gradient accumulation

6. SUPPORTING EVIDENCE:
   - "DistilBERT achieved 71.68% while XLM-RoBERTa 69.24%
      on Spotify app reviews" - showing BERT competitiveness
```

**Referensi:** [Nature Scientific Reports](https://www.nature.com/articles/s41598-025-01104-0)

---

### Pertanyaan E2 [CHALLENGING]
**"FASTopic dan QuaIIT dilaporkan lebih baik dari BERTopic dalam coherence dan diversity. Mengapa tidak mempertimbangkan alternatif ini?"**

#### Expected Answer (Solusi)
```
HONEST ACKNOWLEDGMENT:

1. AWARENESS:
   "Saya aware bahwa FASTopic (NeurIPS 2024) menunjukkan
   performa lebih baik dalam beberapa metrik."

2. JUSTIFICATION FOR BERTOPIC:
   - BERTopic lebih established (2022)
   - Better documentation dan community support
   - Proven untuk Indonesian text (biodiversity study)
   - More modular dan customizable

3. COMPARATIVE PLAN:
   "Saya bersedia menambahkan FASTopic sebagai comparison:
   - BERTopic vs FASTopic vs LDA
   - Evaluate coherence, diversity, interpretability"

4. PRACTICAL CONSIDERATION:
   - BERTopic integration dengan sentiment analysis lebih straightforward
   - Existing frameworks (BERTopic-SKEP) sebagai reference

5. FALLBACK:
   "Jika FASTopic significantly better, saya akan adjust
   methodology di final thesis."
```

**Referensi:** [FASTopic](https://github.com/BobXWu/FASTopic), [Topic Modeling Comparison](https://towardsdatascience.com/choose-the-right-one-evaluating-topic-models-for-business-intelligence/)

---

### Pertanyaan E3
**"Bagaimana Anda memastikan kualitas anotasi data untuk ground truth sentiment? Apa inter-annotator agreement yang Anda targetkan?"**

#### Expected Answer (Solusi)
```
ANNOTATION QUALITY PLAN:

1. ANNOTATOR SELECTION:
   - 2-3 annotators minimum
   - Native Indonesian speakers
   - Training session dengan guidelines

2. ANNOTATION GUIDELINES:
   - Clear definition positive/neutral/negative
   - Example cases
   - Edge case handling

3. PILOT STUDY:
   - 200 reviews untuk pilot
   - Calculate inter-rater reliability
   - Resolve disagreements

4. TARGET METRICS:
   - Cohen's Kappa ≥ 0.6 (substantial agreement)
   - Krippendorff's Alpha ≥ 0.7 (acceptable)

5. DISAGREEMENT RESOLUTION:
   - Discussion untuk controversial cases
   - Third annotator sebagai tiebreaker
   - Document disagreement patterns

6. QUALITY CHECKS:
   - Random spot checks
   - Periodic recalibration

7. REPORTING:
   - Full agreement statistics
   - Class-wise agreement
   - Difficult case analysis
```

**Referensi:** [Inter-rater Reliability](https://imerit.net/resources/blog/human-vs-model-agreement-how-inter-rater-consistency-shapes-benchmark-reliability/)

---

### Pertanyaan E4
**"Jika hasil BERTopic menghasilkan topik yang tidak meaningful atau redundant, apa contingency plan Anda?"**

#### Expected Answer (Solusi)
```
CONTINGENCY PLANS:

1. HYPERPARAMETER TUNING:
   - Systematic search untuk UMAP/HDBSCAN params
   - Use TopicTuner tool

2. ALTERNATIVE EMBEDDING:
   - Try different sentence-transformer models
   - paraphrase-multilingual-MiniLM-L12-v2
   - distiluse-base-multilingual-cased-v2

3. TOPIC REFINEMENT:
   - Merge similar topics manually
   - Remove noise topics (outliers)
   - Hierarchical reduction

4. ALTERNATIVE MODELS:
   - Fallback ke LDA jika BERTopic fails
   - Compare dengan FASTopic
   - Hybrid approach

5. EVALUATION CRITERIA:
   - Coherence score (C_V) > 0.4
   - Topic diversity > 0.5
   - Human interpretability check

6. DOCUMENTATION:
   - Document all attempts
   - Report negative results
   - Analyze failure modes
```

---

# 7. REKOMENDASI METODOLOGI

## 7.1 Proposed Framework

```
┌─────────────────────────────────────────────────────┐
│                 DATA COLLECTION                      │
│  Google Play Scraper → Duolingo Indonesian Reviews   │
│  Filter: 2023-2025, ≥10 words, Indonesian language  │
└─────────────────────────────────────────────────────┘
                          │
                          ▼
┌─────────────────────────────────────────────────────┐
│                  PREPROCESSING                       │
│  Cleaning → Normalization → Slang → (Stemming)      │
└─────────────────────────────────────────────────────┘
                          │
            ┌─────────────┴─────────────┐
            ▼                           ▼
┌───────────────────────┐   ┌───────────────────────┐
│  SENTIMENT ANALYSIS   │   │   TOPIC MODELING      │
│                       │   │                       │
│  IndoBERTweet         │   │  BERTopic             │
│  Fine-tuning          │   │  - Sentence-BERT      │
│  3-class sentiment    │   │  - UMAP + HDBSCAN     │
│                       │   │  - c-TF-IDF           │
└───────────────────────┘   └───────────────────────┘
            │                           │
            └─────────────┬─────────────┘
                          ▼
┌─────────────────────────────────────────────────────┐
│               INTEGRATION ANALYSIS                   │
│  Topic-Sentiment Matrix                             │
│  Per-topic sentiment distribution                   │
│  Temporal analysis                                  │
└─────────────────────────────────────────────────────┘
                          │
                          ▼
┌─────────────────────────────────────────────────────┐
│                   EVALUATION                         │
│  Sentiment: Acc, F1, Precision, Recall              │
│  Topic: Coherence (C_V), Diversity                  │
│  Baseline comparison                                │
└─────────────────────────────────────────────────────┘
```

## 7.2 Evaluation Metrics Summary

| Component | Metric | Target |
|-----------|--------|--------|
| Sentiment Classification | Accuracy | ≥80% |
| Sentiment Classification | F1-Macro | ≥0.75 |
| Sentiment Classification | F1-Weighted | ≥0.80 |
| Topic Modeling | C_V Coherence | ≥0.50 |
| Topic Modeling | Topic Diversity | ≥0.60 |
| Annotation | Krippendorff's α | ≥0.70 |

## 7.3 Tools and Libraries

| Purpose | Tool/Library |
|---------|--------------|
| Data Collection | google-play-scraper |
| Preprocessing | Sastrawi, NLTK, regex |
| Sentiment Model | transformers (HuggingFace) |
| Topic Model | bertopic |
| Embeddings | sentence-transformers |
| Evaluation | scikit-learn, gensim |
| Visualization | matplotlib, seaborn, pyLDAvis |

---

# 8. REFERENSI LENGKAP

## 8.1 IndoBERTweet & IndoBERT

1. Koto, F., Rahimi, A., Lau, J. H., & Baldwin, T. (2021). IndoBERTweet: A Pretrained Language Model for Indonesian Twitter. *EMNLP 2021*. [arXiv](https://arxiv.org/abs/2109.04607)

2. Koto, F., Rahimi, A., Lau, J. H., & Baldwin, T. (2020). IndoLEM and IndoBERT: A Benchmark Dataset and Pre-trained Language Model for Indonesian NLP. *COLING 2020*. [ACL Anthology](https://aclanthology.org/2020.coling-main.66/)

3. Sentiment Analysis Model on Electric Vehicles Using IndoBERTweet and IndoBERT. [Antivirus Journal](https://ejournal.unisbablitar.ac.id/index.php/antivirus/article/view/4416)

4. Performance Analysis of IndoBERT for Sentiment Classification in Indonesian Hotel Review Data. [JOSH Journal](https://ejurnal.seminar-id.com/index.php/josh/article/view/6505)

## 8.2 BERTopic

5. Grootendorst, M. (2022). BERTopic: Neural topic modeling with a class-based TF-IDF procedure. [arXiv](https://arxiv.org/abs/2203.05794)

6. BERTopic Documentation. [Official Docs](https://maartengr.github.io/BERTopic/)

7. BERTopic Analysis of Indonesian Biodiversity Policy on Social Media. [ECTI-CIT](https://ph01.tci-thaijo.org/index.php/ecticit/article/view/255058)

8. Topic Modelling Analysis on Indonesian News Using BERT Topic Model. [IEEE Xplore](https://ieeexplore.ieee.org/document/10903779/)

## 8.3 Duolingo Research

9. Sentiment Analysis and Topic Modeling for Duolingo Application on Google Play Store. [IEEE Xplore](https://ieeexplore.ieee.org/document/10913140/)

10. Sentiment analysis of user reviews: exploring Duolingo and Babbel in English language learning. [Frontiers](https://www.frontiersin.org/journals/computer-science/articles/10.3389/fcomp.2025.1569058/full)

11. Duolingo Language Report 2024. [Duolingo Blog](https://blog.duolingo.com/2024-duolingo-language-report/)

## 8.4 Combined Topic-Sentiment Analysis

12. BERTopic-SKEP for Emergency Management. [Nature Scientific Reports](https://www.nature.com/articles/s41598-025-30319-4)

13. BERTopic + RoBERTa for User Requirements Mining. [PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC11946272/)

14. LDA-Based Topic Modeling Sentiment Analysis Using TDS Model. [MDPI](https://www.mdpi.com/2076-3417/11/23/11091)

## 8.5 Indonesian NLP

15. Indonesian Text Preprocessing. [Medium - Cindy Hosea](https://cindyhosea.medium.com/text-pre-processing-in-bahasa-indonesia-6895154532db)

16. Sastrawi Indonesian Stemmer. [Medium](https://medium.com/@andikahfi98/preprocessing-text-data-in-python-using-nltk-and-sastrawi-ef6b7450b7db)

17. Code-Mixing Normalization. [ACL Anthology](https://aclanthology.org/D19-5554.pdf)

## 8.6 Evaluation & Methodology

18. Topic Coherence Measures. [Towards Data Science](https://towardsdatascience.com/understanding-topic-coherence-measures-4aa41339634c/)

19. BERT Fine-tuning Best Practices. [LinkedIn](https://www.linkedin.com/advice/0/what-best-practices-fine-tuning-bert-sentiment)

20. Inter-rater Reliability in AI. [iMerit](https://imerit.net/resources/blog/human-vs-model-agreement-how-inter-rater-consistency-shapes-benchmark-reliability/)

## 8.7 Alternatives & Comparisons

21. FASTopic: Fast, Adaptive, Stable Topic Model. [GitHub](https://github.com/BobXWu/FASTopic)

22. Topic Modeling Comparison: LDA, NMF, Top2Vec, BERTopic. [PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC9120935/)

23. Cross-Domain Sentiment Analysis. [Taylor & Francis](https://www.tandfonline.com/doi/full/10.1080/09540091.2021.1912711)

## 8.8 App Review Analysis

24. ABSA for App Reviews. [Springer](https://link.springer.com/article/10.1007/s10515-023-00397-7)

25. LLM for App Review Sentiment Analysis. [arXiv](https://arxiv.org/abs/2409.07162)

26. Sentiment Analysis on Google Play Store Reviews. [Springer](https://link.springer.com/article/10.1007/s11042-024-19185-w)

---

# LAMPIRAN

## A. Checklist Pertanyaan Quick Reference

### Must-Ask Questions (Critical)
- [ ] A1: Domain mismatch IndoBERTweet-Twitter vs App Review
- [ ] A2: Novelty vs existing IEEE 2024 research
- [ ] E2: Awareness of FASTopic alternative

### Technical Questions
- [ ] B1: Memory management BERTopic
- [ ] B2: Overfitting mitigation
- [ ] C3: Labeling strategy

### Methodology Questions
- [ ] D1: Expected outputs
- [ ] D3: Baseline comparison plan

## B. Red Flags to Watch

1. **Tidak aware** existing research (IEEE 2024)
2. **Tidak punya plan** untuk domain adaptation
3. **Tidak jelas** evaluation metrics
4. **Tidak pertimbangkan** baseline comparison
5. **Tidak aware** BERTopic limitations

## C. Strong Indicators

1. **Clear justification** untuk method choice
2. **Comparative analysis** plan
3. **Contingency plans** untuk failures
4. **Realistic** timeline dan scope
5. **Understanding** of limitations

---

*Dokumen ini disusun berdasarkan riset komprehensif dari 25+ sumber akademik dan dokumentasi resmi. Tanggal pembuatan: 4 Januari 2026*
