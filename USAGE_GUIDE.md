**注意：本文件內容由 AI 生成。**

# AI-100x-SE-Join-Quest 使用指南

本指南提供了如何設定、運行測試、執行程式碼品質檢查以及生成報告的說明。

## 1. 環境設定

本專案使用 Python 3.11 和 `uv` 作為套件和專案管理器。

1.  **安裝 `uv`**：
    如果您尚未安裝 `uv`，請參考其官方文件進行安裝。

2.  **安裝專案依賴**：
    在專案根目錄下，運行以下命令來安裝所有必要的依賴：
    ```bash
    uv sync
    ```

## 2. 運行測試 (BDD)

本專案使用 `behave` 進行行為驅動開發 (BDD) 測試。

*   **運行所有測試**：
    ```bash
    uv run behave
    ```
*   **運行特定 Feature 或 Scenario**：
    您可以指定要運行的 Feature 檔案或使用標籤來運行特定情境。
    例如：
    ```bash
    uv run behave features/order.feature
    uv run behave --tags @order_pricing
    ```

## 3. 程式碼品質檢查 (Linting & Formatting)

本專案使用 `Ruff` 進行程式碼的 Linting 和格式化。

*   **檢查 Linting 問題**：
    ```bash
    uv run ruff check src/
    ```
*   **自動修復 Linting 問題**：
    ```bash
    uv run ruff check src/ --fix
    ```
*   **格式化程式碼**：
    ```bash
    uv run ruff format src/
    ```
*   **同時修復和格式化**：
    ```bash
    uv run ruff format src/ && uv run ruff check src/ --fix
    ```

## 4. 報告生成

本專案可以生成多種格式的測試報告。

### 4.1 純文字摘要報告

生成一個易於閱讀的純文字測試摘要報告，適合提交到 Git。

*   **生成報告**：
    ```bash
    uv run behave > reports/behave_summary.txt
    ```
*   **報告位置**：`reports/behave_summary.txt`

### 4.2 JSON 格式報告

生成詳細的 JSON 格式測試報告，可用於其他工具生成視覺化報告。

*   **生成報告**：
    ```bash
    uv run behave -f json -o reports/behave_report.json
    ```
*   **報告位置**：`reports/behave_report.json`

### 4.3 Allure HTML 報告

生成美觀且互動性強的 Allure HTML 報告。

1.  **安裝 `allure-behave`**：
    ```bash
    uv pip install allure-behave
    ```
2.  **生成 Allure 結果檔案**：
    ```bash
    uv run behave -f allure_behave.formatter:AllureFormatter -o reports/allure-results features/
    ```
    這會將 Allure 所需的原始結果檔案輸出到 `reports/allure-results` 目錄。

3.  **生成 HTML 報告**：
    您需要確保已安裝 Allure Commandline 工具並在系統 PATH 中。
    ```bash
    allure generate reports/allure-results --clean -o reports/allure-report
    ```
    這會從 `reports/allure-results` 產生 HTML 報告到 `reports/allure-report` 目錄。

4.  **查看 Allure HTML 報告**：
    **重要提示**：您不能直接點擊 `reports/allure-report/index.html` 來查看報告，因為瀏覽器會限制本地檔案的某些功能。您需要透過網頁伺服器來提供服務。
    *   **本地預覽 (推薦)**：
        ```bash
        allure open reports/allure-report
        ```
        這會啟動一個本地伺服器並在瀏覽器中打開報告。
    *   **靜態發布**：
        `reports/allure-report` 目錄的內容是完全靜態的。您可以將此目錄下的所有檔案和子目錄上傳到任何靜態網頁託管服務（例如 GitHub Pages, Netlify, S3 等）進行發布。

## 5. 專案結構概覽

*   `features/`: 包含 Gherkin Feature 檔案 (`.feature`) 和步驟定義 (`steps/` 目錄)。
*   `src/`: 包含專案的原始程式碼。
*   `reports/`: 存放生成的測試報告。
*   `pyproject.toml`: 專案的設定檔，包含依賴和專案元數據。
*   `uv.lock`: `uv` 生成的鎖定檔案，確保依賴版本一致性。
