from telegraph import Telegraph as tele_graph


class Telegraph:
    def Write(text , question):
        """Write Into Telegraph

        Args:
            text (str): Text
            question (str): Ask Your Ask
        """
        telegraph = tele_graph()
        telegraph.create_account(short_name='YudhoPRJKT(by YudhoPatrianto)')
        response_telegraph = telegraph.create_page(
            title=question,
            author_name='YudhoPatrianto',
            html_content=text
        )['path']
        result_link = f'https://telegra.ph/{response_telegraph}'
        return result_link