;; ツールバーを非表示に
(tool-bar-mode -1)
;; バックアップを残さない
(setq make-backup-files nil)
;; C-Ret で矩形選択
;; 詳しいキーバインド操作：http://dev.ariel-networks.com/articles/emacs/part5/
(cua-mode t)
(setq cua-enable-cua-keys nil)

;; 起動時の画面を非表示
(setq inhibit-startup-message t)
;; 現在の行をハイライト表示する
(global-hl-line-mode)
(show-paren-mode t)
;; カーソルの色をオレンジ色に設定する (白色なら white にする)
(setq default-frame-alist
      (append (list '(cursor-color . "orange")) default-frame-alist))

;; 10秒間操作をしない場合は、2秒周期でカーソルを明滅
;;(set-cursor-color "orange")
;; (setq blink-cursor-interval 1.0)
;; (setq blink-cursor-delay 10.0)
;; (blink-cursor-mode 1)

;; key-bind 設定　;;
(global-set-key "\M-n" 'linum-mode)
(global-set-key "\M-g" 'goto-line)

;;行数表示
(global-linum-mode t)
;;ビープ音を消す
(setq ring-bell-function 'ignore)


(setq default-input-method "MacOSX")
;; Monaco 12pt をデフォルトにする
(set-face-attribute 'default nil
                    :family "Monaco"
                    :height 130)
;; 日本語をヒラギノ角ゴProNにする
(set-fontset-font "fontset-default"
                  'japanese-jisx0208
                  '("Hiragino Maru Gothic ProN"))
;; 半角カナをヒラギノ角ゴProNにする
(set-fontset-font "fontset-default"
                  'katakana-jisx0201
                  '("Hiragino Maru Gothic ProN"))

;; minibuffer 内は英数モードにする
;; (add-hook 'minibuffer-setup-hook 'mac-change-language-to-us)
;; (mac-translate-from-yen-to-backslash)
(define-key global-map [?¥] [?\\])
				  
;; markdown-mode http://jblevins.org/projects/markdown-mode/
;; cd ~/.emacs.d/; git clone git://jblevins.org/git/markdown-mode.git
(setq load-path (append '("~/.emacs.d/markdown-mode") load-path))
(add-to-list 'load-path "~/.emacs.d/site-lisp")
(autoload 'markdown-mode "markdown-mode"
   "Major mode for editing Markdown files" t)
(add-to-list 'auto-mode-alist '("\\.text\\'" . markdown-mode))
(add-to-list 'auto-mode-alist '("\\.markdown\\'" . markdown-mode))
(add-to-list 'auto-mode-alist '("\\.md\\'" . markdown-mode))

;; http://moya-notes.blogspot.jp/2013/02/emacs24-config-on-mac.html#markdown2
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;; [基本] トラックパッド用のスクロール設定
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
(defun scroll-down-with-lines ()
  "" (interactive) (scroll-down 3))
(defun scroll-up-with-lines ()
  "" (interactive) (scroll-up 3))
(global-set-key [wheel-up] 'scroll-down-with-lines)
(global-set-key [wheel-down] 'scroll-up-with-lines)
(global-set-key [double-wheel-up] 'scroll-down-with-lines)
(global-set-key [double-wheel-down] 'scroll-up-with-lines)
(global-set-key [triple-wheel-up] 'scroll-down-with-lines)
(global-set-key [triple-wheel-down] 'scroll-up-with-lines)

;; http://sakito.jp/emacs/emacs23.html#id21
(define-key global-map [ns-drag-file] 'ns-find-file)
;; http://www.emacswiki.org/emacs/TransparentEmacs
;;(set-frame-parameter (selected-frame) 'alpha '(<active> [<inactive>]))
;; (set-frame-parameter (selected-frame) 'alpha '(95 50))
;;(add-to-list 'default-frame-alist '(alpha 95 50))

;; auto-complete を設定する
(require 'auto-complete)
(require 'auto-complete-config)    ;; 必須ではないですが一応
(global-auto-complete-mode t)
;; (global ac-complete-mode-map "\M-TAB" 'ac-next)
;; (define-key ac-complete-mode-map "\C-n" 'ac-next)
;; (define-key ac-complete-mode-map "\C-p" 'ac-previous)

(package-initialize)
(add-to-list 'package-archives 
	     '("melpa" . "http://melpa.milkbox.net/packages/") t)
(add-to-list 'package-archives
	     '("marmalade" . "http://marmalade-repo.org/packages/") t)

(add-to-list 'auto-mode-alist '("\\.rb\\'" . enh-ruby-mode))
(add-to-list 'auto-mode-alist '("\\.erb\\'" . enh-ruby-mode))

(setq c-mode-hook
      '(lambda ()
	 (setq c-basic-offset 4)
	 (setq tab-width 4)
	))
(custom-set-variables
 ;; custom-set-variables was added by Custom.
 ;; If you edit it by hand, you could mess it up, so be careful.
 ;; Your init file should contain only one such instance.
 ;; If there is more than one, they won't work right.
 '(package-selected-packages (quote (web-mode enh-ruby-mode))))
(custom-set-faces
 ;; custom-set-faces was added by Custom.
 ;; If you edit it by hand, you could mess it up, so be careful.
 ;; Your init file should contain only one such instance.
 ;; If there is more than one, they won't work right.
 )
