import React from 'react';
import {AbsoluteFill, interpolate, spring, useCurrentFrame, useVideoConfig} from 'remotion';

const AMBER = '#f2a900';
const GREEN = '#6fcf7f';
const BLUE = '#6aa7ff';
const PANEL_TOP = 560;
const ROW_H = 170;
const GAP = 20;
const rowTop = (i: number) => PANEL_TOP + i * (ROW_H + GAP);

const base = [
  ['Клиент А', 'Расчёт', 'В работе', 'Звонок сегодня'],
  ['Клиент Б', 'Консультация', 'Новая', 'Ответить до 18:00'],
  ['Клиент В', 'Повторный заказ', 'В работе', 'Отправить счёт'],
  ['Клиент Г', 'Расчёт', 'Без ответа', '3 дня без ответа'],
  ['Клиент Д', 'Консультация', 'Закрыта', 'Готово'],
];

const clamp = {extrapolateLeft: 'clamp', extrapolateRight: 'clamp'} as const;
const ease = (t: number, a: number, b: number, from = 0, to = 1) => interpolate(t, [a, b], [from, to], clamp);

export const Demo: React.FC = () => {
  const f = useCurrentFrame();
  const {fps} = useVideoConfig();
  const t = f / fps;

  // phases for the hot row (index 3)
  const phase = t < 8 ? 0 : t < 11 ? 1 : 2;

  // other rows dim from 2.0 s, everything dims at 14 s
  const dimOthers = ease(t, 2, 2.4, 1, 0.28);
  const endDim = ease(t, 14, 14.4, 1, 0.05);
  const othersOpacity = Math.min(dimOthers, endDim);
  const hotOpacity = endDim;

  const pulse = t > 1 && t < 1.6 ? 1 + 0.03 * Math.sin(((t - 1) / 0.6) * Math.PI) : 1;
  const ring = ease(t, 2.2, 2.6);

  // plate text per segment
  const segs: [number, string][] = [
    [0, 'Заявка зависла. Вы заметите?'],
    [2, 'Вот эта. Три дня тишины.'],
    [5, 'Берёте в работу'],
    [8, 'Назначили шаг и срок'],
    [11, 'Закрыта, а не забыта'],
    [14, 'Хотите так же? Напишите в директ'],
  ];
  let seg = 0;
  segs.forEach(([s], i) => { if (t >= s) seg = i; });
  const segStart = segs[seg][0] * fps;
  const local = f - segStart;
  const plateIn = seg === 0 ? 1 : spring({frame: local, fps, config: {damping: 200}, durationInFrames: 10});
  const plateY = seg === 0 ? 0 : (1 - plateIn) * 24;

  // pointer path
  const pts: [number, number, number][] = [
    [4.8, 980, 1000], [5.8, 905, 1190], [6.3, 905, 1190], [6.9, 860, 1400], [7.3, 860, 1400], [7.8, 940, 1560], [8.2, 940, 1560],
  ];
  const px = interpolate(t, pts.map(p => p[0]), pts.map(p => p[1]), clamp);
  const py = interpolate(t, pts.map(p => p[0]), pts.map(p => p[2]), clamp);
  const pointerVisible = t > 4.8 && t < 8.0 ? 1 : 0;
  const click = t > 7.2 && t < 7.4;

  // dropdown
  const dropOpen = t > 6.0 && t < 7.5;
  const dropOpts = ['Новая', 'В работе', 'Закрыта'];

  // hot row content
  let status = base[3][2];
  let next = base[3][3];
  let statusColor = AMBER;
  let bg = '#3a2c06';
  let border = AMBER;
  if (phase === 1) {
    status = 'В работе'; statusColor = BLUE; bg = '#16253d'; border = BLUE;
    const full = 'Позвонить завтра 10:00';
    const n = Math.floor(ease(t, 8.5, 10.3, 0, full.length));
    next = full.slice(0, n) + (n < full.length ? '▍' : '');
  } else if (phase === 2) {
    status = 'Закрыта'; statusColor = GREEN; bg = '#12301d'; border = GREEN; next = 'Готово';
  }
  const badge = phase === 1 ? spring({frame: f - 8 * fps, fps, config: {damping: 9, stiffness: 160}}) : phase === 2 ? spring({frame: f - 11 * fps, fps, config: {damping: 9, stiffness: 160}}) : 1;
  const badgeScale = phase === 0 ? 1 : 0.6 + 0.4 * Math.min(badge, 1.15);

  const stuck = phase === 2 ? 0 : 1;
  const hotTransform = phase === 0 ? `scale(${pulse})` : undefined;

  const showCta = t >= 14;
  const handleIn = ease(t, 14.3, 14.8);

  return (
    <AbsoluteFill style={{background: '#101418', fontFamily: 'DejaVu Sans, sans-serif', color: '#fff'}}>
      {/* plate: top fifth */}
      <div style={{position: 'absolute', top: 170, left: 60, right: 60, minHeight: 200, display: 'flex', alignItems: 'center', background: showCta ? GREEN : AMBER, color: '#101418', fontSize: 66, fontWeight: 800, padding: '30px 44px', borderRadius: 28, lineHeight: 1.15, opacity: plateIn, transform: `translateY(${plateY}px)`}}>
        {segs[seg][1]}
      </div>

      {/* header: counter + demo tag (always visible) */}
      <div style={{position: 'absolute', top: 470, left: 40, right: 40, display: 'flex', justifyContent: 'space-between', alignItems: 'center', fontSize: 40}}>
        <div style={{opacity: endDim, fontWeight: 700, color: stuck ? AMBER : GREEN}}>Зависших: {stuck}</div>
        <div style={{opacity: 0.75, fontSize: 34, border: '2px solid #ffffff55', borderRadius: 14, padding: '6px 18px'}}>Демо-данные</div>
      </div>

      {/* rows */}
      {base.map((r, i) => {
        const hot = i === 3;
        return (
          <div key={i} style={{
            position: 'absolute', left: 40, right: 40, top: rowTop(i), height: ROW_H,
            display: 'flex', alignItems: 'center', justifyContent: 'space-between', padding: '0 36px',
            borderRadius: 26, fontSize: 46,
            background: hot ? bg : '#1c232b',
            border: hot ? `${4 + (phase === 0 ? ring * 6 : 0)}px solid ${border}` : '4px solid transparent',
            opacity: hot ? hotOpacity : othersOpacity,
            transform: hot ? hotTransform : undefined,
          }}>
            <div><div style={{fontWeight: 700}}>{r[0]}</div><div style={{fontSize: 34, opacity: 0.7}}>{r[1]}</div></div>
            <div style={{textAlign: 'right'}}>
              <div style={{fontWeight: 700, color: hot ? statusColor : GREEN, display: 'inline-block', transform: hot ? `scale(${badgeScale})` : undefined, transformOrigin: 'right center'}}>{hot ? status : r[2]}</div>
              <div style={{fontSize: 34, opacity: 0.85}}>{hot ? next : r[3]}</div>
            </div>
          </div>
        );
      })}

      {/* dropdown */}
      {dropOpen && (
        <div style={{position: 'absolute', left: 560, width: 460, top: 1310, background: '#2a333d', borderRadius: 22, border: '3px solid #ffffff33', overflow: 'hidden', fontSize: 44, boxShadow: '0 20px 40px #000a'}}>
          {dropOpts.map((o, i) => (
            <div key={o} style={{height: 70, display: 'flex', alignItems: 'center', padding: '0 30px', background: o === 'В работе' && t > 6.8 ? (click ? AMBER : '#3b4754') : undefined, color: o === 'В работе' && click ? '#101418' : '#fff'}}>{o}</div>
          ))}
        </div>
      )}

      {/* pointer */}
      {pointerVisible ? (
        <svg width="70" height="70" viewBox="0 0 24 24" style={{position: 'absolute', left: px, top: py, filter: 'drop-shadow(0 4px 6px #000a)'}}>
          <path d="M3 2 L3 19 L8 14.5 L11.5 22 L14.5 20.6 L11 13.3 L18 13.3 Z" fill="#fff" stroke="#101418" strokeWidth="1.2" />
        </svg>
      ) : null}

      {/* end card: handle */}
      {showCta && (
        <div style={{position: 'absolute', top: 1344 - 60, left: 0, right: 0, textAlign: 'center', fontSize: 76, fontWeight: 800, opacity: handleIn}}>
          @nosignoutside
        </div>
      )}
    </AbsoluteFill>
  );
};
