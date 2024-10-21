import io
import sys
import textwrap

class Run:
    @staticmethod
    def PythonTerminal(command_in):
        corrected_command_indent = textwrap.dedent(command_in)
        
        # Membuat StringIO untuk menangkap output
        output_command = io.StringIO()
        
        # Menyimpan stream asli
        original_stdout = sys.stdout
        original_stderr = sys.stderr
        
        # Mengalihkan stdout dan stderr ke output_command
        sys.stdout = output_command
        sys.stderr = output_command
        
        error_message = ""
        try:
            exec(corrected_command_indent)
        except Exception as e:
            # Menyimpan pesan error sebagai string
            error_message = str(e)
        finally:
            # Mengembalikan stream asli
            sys.stdout = original_stdout
            sys.stderr = original_stderr
        
        # Menggabungkan output dan error dalam satu string
        return output_command.getvalue() + ("\n" + error_message if error_message else "")
