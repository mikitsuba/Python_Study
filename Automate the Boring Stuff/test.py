#!/usr/bin/env python3

import logging

logging.basicConfig(level=logging.DEBUG,
format=' %(asctime)s - %(levelname)s - %(message)s')

logging.disable(logging.CRITICAL)

logging.debug('デバック用詳細情報')

logging.info('loggingモジュールは動作中')

logging.warning('エラーメッセージがログ出力されようとしている')

logging.error('エラーが発生した')

logging.critical('プログラムは回復不能！')
