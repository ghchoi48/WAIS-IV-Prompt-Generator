# Manual Testing Guide for History Feature

## Test Case 1: Verify History Saving and Viewing

1.  **Run the application.**
2.  **Generate First Prompt:**
    *   Enter some unique data into the input fields (e.g., Age: 30, FSIQ: 100).
    *   Click the "프롬프트 생성" (Generate Prompt) button.
    *   Verify the prompt appears in the main text area.
3.  **Generate Second Prompt:**
    *   Change the input data to something different (e.g., Age: 45, FSIQ: 110).
    *   Click the "프롬프트 생성" (Generate Prompt) button again.
    *   Verify the new prompt appears in the main text area.
4.  **Check `history.txt` (Optional but Recommended):**
    *   Open the `history.txt` file (it should be in the same directory as the application or in the `Sources` directory if the application is run from there).
    *   Verify that it contains the two prompts generated, each on a new line.
5.  **View History via UI:**
    *   Click the "기록 보기" (View History) button.
    *   A dialog window titled "기록 보기" should appear.
    *   Verify that this dialog displays the two prompts generated earlier. The text should be read-only.
    *   Click the "닫기" (Close) button in the dialog. The dialog should close.
6.  **Generate Third Prompt (Post History View):**
    *   Enter new data (e.g., Age: 22, FSIQ: 95).
    *   Click the "프롬프트 생성" (Generate Prompt) button.
7.  **View History Again:**
    *   Click the "기록 보기" (View History) button again.
    *   Verify that the dialog now displays all three prompts (the two old ones and the new one).
    *   Close the dialog.

## Test Case 2: Verify Behavior with No History

1.  **Ensure no `history.txt` file exists.** (Delete it if it was created from previous tests).
2.  **Run the application.**
3.  **View History:**
    *   Click the "기록 보기" (View History) button.
    *   A message box should appear stating "기록 파일(history.txt)을 찾을 수 없습니다." (History file (history.txt) not found.) or "기록이 없습니다." (No history found) if the file was created but empty by another action. Click OK/Close on the message box.
4.  **Generate a Prompt:**
    *   Enter any data and click "프롬프트 생성".
5.  **View History:**
    *   Click "기록 보기".
    *   The dialog should now appear and show the single prompt you just generated.
    *   Close the dialog.
