REM create a new conda environment
conda create -n cert python=3.5 -y

REM activate environment
call conda activate cert

REM install two dependencies not included with base python
pip install reportlab==3.5.19 --force-reinstall
pip install PyPDF2==1.26.0 --force-reinstall
