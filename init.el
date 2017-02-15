;; ツールバーを非表示に
(tool-bar-mode -1)
;; バックアップを残さない
(setq make-backup-files nil)
;; C-Ret で矩形選択
(cua-mode t)
(setq cua-enable-cua-keys nil)
;; 起動時の画面を非表示
(setq inhibit-startup-message t)
;; 現在の行をハイライト表示する
(global-hl-line-mode)
;; カッコを対応付け
(show-paren-mode t)
;; カーソルの色をオレンジ色に設定する (白色なら white にする)
(setq default-frame-alist
      (append (list '(cursor-color . "orange")) default-frame-alist))

;; key-bind 設定
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
(add-hook 'minibuffer-setup-hook 'mac-change-language-to-us)

;; ￥を\に変換
(define-key global-map [?¥] [?\\])
				  
(add-to-list 'load-path "~/.emacs.d/site-lisp")

;; ウィンドウの透明度の設定
(add-to-list 'default-frame-alist '(alpha . 75))

;; auto-complete を設定する
(require 'auto-complete)
(require 'auto-complete-config)    ;; 必須ではないですが一応
(global-auto-complete-mode t)

(require 'package)
;; (add-to-list 'package-archives 
;; 	     '("melpa" . "http://melpa.milkbox.net/packages/") t)
(add-to-list 'package-archives 
	     '("melpa" . "https://melpa.org/packages/") t)
(add-to-list 'package-archives
	     '("marmalade" . "http://marmalade-repo.org/packages/") t)
(package-initialize)

(add-to-list 'auto-mode-alist '("\\.rb\\'" . enh-ruby-mode))
(add-to-list 'auto-mode-alist '("\\.erb\\'" . enh-ruby-mode))

(setq c-mode-hook
      '(lambda ()
	 (setq c-basic-offset 4)
	 (setq tab-width 4)
	))
(custom-set-variables
 '(package-selected-packages (quote (auctex auto-complete fzf web-mode enh-ruby-mode))))
(custom-set-faces)

(add-hook 'LaTeX-mode-hook
	  '(lambda ()
	     (TeX-fold-mode 1)))
(add-hook 'LaTeX-mode-hook
	  'turn-on-reftex)
(setq reftex-plug-into-AUCTeX t)
(add-hook 'reftex-mode-hook
	  '(lambda ()
	     (define-key reftex-mode-map (kbd "\C-cr") 'reftex-reference)
	     (define-key reftex-mode-map (kbd "\C-cl") 'reftex-label)
	     (define-key reftex-mode-map (kbd "\C-cc") 'reftex-citation)
	     ))


(add-to-list 'load-path
	     (expand-file-name "~/.emacs.d/elpa/yasnippet-20161221.1953/"))
(require 'yasnippet)
;; (setq yas-snippet-dirs
;;       '("~/.emacs.d/mysnippets"
;;       '("~/.emacs.d/yasnippets"))
      
(define-key yas-minor-mode-map (kbd "C-x i i") 'yas-insert-snippet)
(define-key yas-minor-mode-map (kbd "C-x i n") 'yas-new-snippet)
(define-key yas-minor-mode-map (kbd "C-x i v") 'yas-visit-snippet-file)

(yas-global-mode 1)

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;; [基本] トラックパッド用のスクロール設定
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
(defun scroll-down-with-lines ()
  "" (interactive) (scroll-down 3))
(defun scroll-up-with-lines ()
  "" (interactive) (scroll-up 3))
(global-set-key [double-wheel-up] 'scroll-down-with-lines)
(global-set-key [double-wheel-down] 'scroll-up-with-lines)
