# WEEKLY PROGRESS JOURNAL
### *Repair Flow – Right-to-Repair Assistant & Reparability Portal*

**Name:** Punya Chhabra
**Roll No:** 1024030684
**Course:** UCS503P (Software Engineering)
**Team:** Punya Chhabra, Arnav Gupta, Kaushik Jindal

## Week 1 (Aug 3 - Aug 9): Project Ideation & Team Meetings
- Formed the project team for the UCS503P Software Engineering course.
- Held team meetings and discussions to brainstorm project ideas around the right-to-repair movement and the growing e-waste problem.
- Prepared the initial pitch presentation introducing the project idea and problem statement.

## Week 2 (Aug 10 - Aug 16): Project Proposal Drafting
- Held further discussions to refine the problem statement and the proposed solution.
- Contributed to drafting the full project proposal, with a focus on scoping the RAG (Retrieval-Augmented Generation) module for laptop repair guidance.

## Week 3 (Aug 17 - Aug 23): RAG Module Setup & Design
- Researched RAG pipeline approaches suited to retrieving laptop repair guides and documentation.
- Defined the ingestion and chunking strategy to be used for repair guide documents.

## Week 4 (Aug 24 - Aug 30): Ingestion, Chunking & Embedding Pipeline
- Implemented the document ingestion pipeline, including chunking and embedding generation.
- Created two placeholder repair guide documents (hinge repair, battery replacement) to test the pipeline.

## Week 5 & Week 6 (Aug 31 - Sep 12): Retrieval, Evaluation Metrics & CI/CD
- Implemented the retrieval module on top of ChromaDB, returning relevant chunks for a given repair query.
- Set up a GitHub Actions CI workflow running ruff linting and pytest to satisfy the proposal's CI/CD and testing commitments.

## MST Break (Sep 12 - Oct 3): Mid-Sem Examinations
- Paused project work for the Mid-Semester Tests (MST) and focused on exam preparation.

## Week 7 (Oct 4 - Oct 10): Corpus Scaling via iFixit API
- Built `ifixit_source.py` to pull additional laptop repair guides from the iFixit API and grow the corpus beyond the two placeholder guides.
- Fixed CI/CD pipeline issues caused by the project's subfolder restructuring, including updating the working-directory setting in the CI workflow.

## Week 8 (Oct 11 - Oct 17): Retrieval Calibration
- Built `calibrate.py` to determine the maximum retrieval distance (similarity threshold) at which the RAG system should still attempt to answer a query.

## Week 9 (Oct 18 - Oct 24): API Layer & Answer Generation
- Built `api.py` to expose the RAG pipeline through an API layer.
- Implemented `generate.py` and configured the LLM API key to complete the answer-generation step of the pipeline.

## Week 10 (Oct 25 - Oct 31): Evaluation & GitHub-page Updates
- Compared naive RAG against hybrid search for the project's corpus and confirmed naive RAG remains sufficient for the current scope.
- Built `evaluate.py` to evaluate the RAG pipeline's retrieval and answer quality.
- Updated progress on the project's GitHub Pages site.
