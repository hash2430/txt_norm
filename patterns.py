#-*- coding: utf-8 -*-

eng_unit_pattern = "[ ]?(cm|mm|m|km|g|kg|Hz|KHz|GHz)"
other_unit_pattern = "[ ]?(%|℃|㎓)"
number_pattern = "([+-]?\d[\d,]*)[\.]?\d*"
count_pattern = "[ ]?(가지|마리|송이)"
quote_pattern = """([`"'＂“‘])(.+?)([`"'＂”’])"""
alphabet_pattern = '[A-Z]+'