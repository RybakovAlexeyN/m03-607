# Как пользоваться Handwriting Notes

Подготовьте текст конспекта в `.txt` / `.md` и 3–7 фотографий **своего** почерка. Можно использовать чужие образцы только с разрешения автора.

В агенте, поддерживающем skills и генерацию изображений по референсам, подключите папку `handwriting-notes` и скажите:

> Используй handwriting-notes. Сделай страницы А4 из моего точного текста по фотографиям моего почерка. Режим precision, синие чернила, две колонки. Генерируй по странице и проверяй отсутствие ошибок и повторов.

### Python
```bash
python3 handwriting-notes/scripts/pagepack.py prepare my-notes.txt --out work --mode precision --layout two_columns --max-chars 1300
```
Результат: `work/original.txt`, `work/pages/`, `work/prompts/`, `work/manifest.json`. Приложите текст каждого промпта и фото к генератору изображений. Готовые страницы сохраните в `work/renders/page-01.png` и т. д.

```bash
python3 handwriting-notes/scripts/pagepack.py verify work --images work/renders
```

Проверка находит отсутствующие файлы, а при установленном Pillow — подозрительно похожие изображения. **Она не проверяет буквы на картинке.** Для посимвольной проверки вручную перепишите прочитанный текст в `work/transcriptions/page-XX.txt` и запустите `verify work --transcriptions work/transcriptions`.

Проверяйте правила преподавателя: цифровой конспект нельзя выдавать за доказательство физического рукописного выполнения. Не публикуйте фотографии чужого почерка.