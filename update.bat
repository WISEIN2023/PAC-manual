@echo off
chcp 65001 > nul
REM PAC 매뉴얼 저장소 갱신 스크립트 (Windows)
REM 원본 DOCX 폴더 경로 - 환경에 맞게 수정하세요
set PAC_DOCX_SRC=E:\700. PAC 메뉴얼관리\PAC Manual(DOCX)

echo.
echo 원본 폴더: %PAC_DOCX_SRC%
echo.
python "%~dp0tools\update.py"
if errorlevel 1 (
  echo.
  echo 갱신에 실패했습니다. 위 메시지를 확인하세요.
  pause
  exit /b 1
)
echo.
echo 변경된 파일 목록:
git status --short
echo.
pause
